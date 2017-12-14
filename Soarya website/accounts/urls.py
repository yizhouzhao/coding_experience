#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:22:10 2017

@author: yizhouz
"""

from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^register/$',views.register,name = 'register'),
    url(r'^signup/$',views.signup,name = 'signup'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]