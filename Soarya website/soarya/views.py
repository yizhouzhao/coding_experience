# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required

#About time
from django.utils import timezone
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from soarya.models import Category,Course,Source,ContactMessage,Comment


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django import forms
from soarya.forms import ContactForm,CommentForm
# Create your views here.

#----indexilize views
def Index(request):
    category_list = Category.objects.order_by('-rank')[:5]

    context_dict = {'categories': category_list}
    return render(request,'soarya/index.html',context_dict)


def About(request):
    return render(request,'soarya/about.html',{})

def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            newMessage = ContactMessage.objects.create(message = form.cleaned_data['message'],
                            email = form.cleaned_data['email'],name = form.cleaned_data['name'])
            newMessage.save()
            return HttpResponseRedirect(reverse('soarya:thanks'))
    else:
        form = ContactForm()

    return render(request,'soarya/contact.html',{'form':form})
    #return render(request,'soarya/contact.html',{})

def Coming(request):
    return render(request,'soarya/coming.html',{})

def Thanks(request):
    return render(request,'soarya/thanks.html',{})


#----Subject
def Subject(request,subject_slug):
    category = Category.objects.get(slug = subject_slug)
    #print(category.name)
    courses = Course.objects.filter(category__name__contains=category.name)
    
    context_dict = {'category': category,'courses':courses}
    return render(request,'soarya/list.html',context_dict)

def Lesson(request,subject_slug,course_slug):
    course = Course.objects.get(slug = course_slug)
    sources = Source.objects.filter(course__name__contains=course.name)
    tutorials = sources.filter(label='tutorial')[:5]
    books =sources.filter(label='book')[:6]
    blogs = sources.filter(label='blog')[:5]
    courses = sources.filter(label='course')[:5]


    #print(subject_slug,course_slug,'books')
    context_dict = {'subject_slug':subject_slug,'course_slug':course.slug,
                    'course':course,
                    'courses':courses,'tutorials':tutorials,'books':books,
                    'blogs':blogs}
    return render(request,'soarya/content.html',context_dict)

def More(request,subject_slug,course_slug,label):
    sources_list = Source.objects.filter(course__slug__contains=course_slug,label=label[:-1]) #books -> book
    paginator = Paginator(sources_list, 8)
    page = request.GET.get('page',1)
    #print(page)

    try:
        sources = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sources = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sources = paginator.page(paginator.num_pages)

    #print(sources_list)
    return render(request, 'soarya/moretable.html', {'sources':sources,'course_slug':course_slug,'label':label})



def CommentOn(request,subject_slug,course_slug,source_id):
    source = Source.objects.get(id = source_id)
    comments_list = Comment.objects.filter(target__id = source_id).order_by('-like') # books -> book
    paginator = Paginator(comments_list, 10)
    page = request.GET.get('page', 1)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                newComment= Comment.objects.create(content = form.cleaned_data['content'],
                                score = form.cleaned_data['score'],difficulty = form.cleaned_data['difficulty'],
                                target = source, owner=request.user)
                newComment.save()
                return HttpResponseRedirect(reverse('soarya:thanks'))
    else:
        form = ContactForm()


    return render(request, 'soarya/comment.html', {'comments':comments,'source':source})


def Addsoarya(request):

    back_to = request.POST.get('next', '/')

    label_dic = [('tutorial','Tutorial'),('book','Book'),('blog','Blog'),('course','Course')]

    categories = Category.objects.all()
    categories_names = tuple([(str(i),categories[i].name) for i in range(len(categories))])
    #print(categories_names)
    courses = Course.objects.all()
    courses_names = [(str(i), courses[i].name) for i in range(len(courses))]

    class AddForm(forms.Form):
        category = forms.ChoiceField(choices = categories_names)
        course = forms.ChoiceField(choices=courses_names)
        label = forms.ChoiceField(choices = label_dic)
        name = forms.CharField(max_length=100)
        link = forms.URLField()
        author = forms.CharField(max_length = 100)
        description = forms.CharField(
            max_length=1200,
            widget=forms.Textarea(),
            help_text='optional',
            required=False
        )
        score = forms.IntegerField(min_value=0, max_value=5)
        difficulty = forms.IntegerField(min_value=0, max_value=5)

    if request.method == 'POST':
        add_form = AddForm(request.POST)
        if add_form.is_valid():
            cate = categories_names[int(add_form.cleaned_data['category'])][1]
            cour = courses_names[int(add_form.cleaned_data['course'])][1]
            name = add_form.cleaned_data['name']
            link = add_form.cleaned_data['link']
            auth = add_form.cleaned_data['author']
            scor = add_form.cleaned_data['score']
            diff = add_form.cleaned_data['difficulty']

            category = Category.objects.get(name=cate)
            course = Course.objects.get(name=cour)
            source = Source.objects.get_or_create(name=name, category=category, course=course)[0]
            source.author = auth
            source.link = link
            source.label = add_form.cleaned_data['label']
            source.save()

            #return HttpResponseRedirect(back_to)
            return HttpResponseRedirect(reverse('soarya:index'))


    else:
         add_form = AddForm()

    return render(request, 'soarya/add.html', {'form':add_form})

