# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,Course,Source,Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Source)
admin.site.register(Comment)