#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:50:22 2017

@author: yizhouz
"""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'julso.settings')

import django

django.setup()


from soarya.models import Category, Course,Source
#populate soarya

def PopuCata():
    f = open("populate/catagory.txt","r")
    for line in f.readlines():
        line = line.strip()
        print line
        subject,state = Category.objects.get_or_create(name = line)
        subject.save()
        

def PopuCourse():
    f = open("populate/course.csv","r")
    #f.next()
    for count,line in enumerate(f.readlines()):
        if count == 0: continue
        line = line.strip()
        info = line.split(",")
        print(info)
        subject,state = Category.objects.get_or_create(name = info[1])
        print("re",subject.name,state)
        lesson,state = Course.objects.get_or_create(
                name = info[0], category = subject)
        lesson.save()
        print(state)


def PopuSource():
    f = open("populate/source.csv","r")
    for count,line in enumerate(f.readlines()):
        line = line.strip()
        info = line.split(",")
        try:
            category = Category.objects.get(name = info[6])
            course = Course.objects.get(name = info[7])
            source = Source.objects.get_or_create(name = info[2],category=category,course=course)[0]
            source.author = info[3]
            source.link = info[4]
            source.label = info[5]
            source.save()
        except:
            print("Error in line",count)
        #print(info)


if __name__ == '__main__':
    print "Start populating: \n\n"
    #PopuCata()
    PopuSource()
    print("End populating \n\n")
