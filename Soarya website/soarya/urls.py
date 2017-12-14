#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:22:10 2017

@author: yizhouz
"""

from django.conf.urls import url
from . import views

app_name = 'soarya'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^about/$',views.About, name = 'about'),
    url(r'^contact/$',views.Contact,name = 'contact'),
    url(r'^coming/$',views.Coming,name = 'coming'),
    url(r'^thanks/$',views.Thanks,name = 'thanks'),
    url(r'^addsoarya/$',views.Addsoarya,name='addsoarya'),
    url(r'^(?P<subject_slug>[\w\-]+)/$',views.Subject,name = 'subject'),
    url(r'^(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/$',
        views.Lesson,name = 'lesson'),

    url(r'^(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<label>(books|tutorials|blogs|courses)+)/$',views.More,name='more'),
    url(r'^(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<source_id>[\w]+)/comments$',views.CommentOn, name='comments'),
]