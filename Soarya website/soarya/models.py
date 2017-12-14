# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from accounts.models import UserProfile
import datetime

from django.db import models
from django.template.defaultfilters import slugify

from accounts.models import User, UserProfile

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    rank = models.IntegerField(default = 0)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    
class Course(models.Model):    
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category)
    rank = models.IntegerField(default = 0)
    column = models.IntegerField(default=0) #position for which column of listing
    
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'courses'
    def __str__(self):
        return self.name
    
class Source(models.Model):
    name = models.CharField(max_length = 200) #简称 #must have name
    #id is set automatically by django
    description = models.CharField(max_length = 2000, blank = True)
    author = models.CharField(max_length= 100, blank = True)
    link = models.URLField(max_length = 200,default = "") #must have link
    label = models.CharField(max_length = 50,blank = True)
    category = models.ForeignKey(Category) #must have
    course = models.ForeignKey(Course)
    difficulty = models.IntegerField(default = 3)
    difficulty_num = models.IntegerField(default = 1)
    score = models.IntegerField(default = 3)
    score_num = models.IntegerField(default = 1)
    pub_date = models.DateTimeField(default=timezone.now) # must have, generate automatically
    #valid_date = models.DateTimeField(blank = True)
    comment_num = models.IntegerField(default = 0)
    comment_on = models.BooleanField(default = True)
    clicks = models.IntegerField(default = 0)
    valid = models.BooleanField(default = True) #whether is valid
    owner = models.ForeignKey(User,null=True) #must have an owner
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Source, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'sources'
        
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    content = models.CharField(max_length=2048,default="")  # comment
    owner = models.ForeignKey(User) #who posted
    pub_date = models.DateTimeField(default=timezone.now) #date
    like = models.IntegerField(default = 0) #pike
    target = models.ForeignKey(Source)#target

    score = models.IntegerField(default=3)
    difficulty = models.IntegerField(default=2)


class ContactMessage(models.Model):
    message = models.CharField(max_length=1000, default="")
    email = models.EmailField(max_length = 254, blank=True)
    name = models.CharField(max_length=128, blank=True)


