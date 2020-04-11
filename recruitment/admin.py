# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Questions, Sith , Recruit

admin.site.register(Questions)
admin.site.register(Recruit)
admin.site.register(Sith)
# Register your models here.
