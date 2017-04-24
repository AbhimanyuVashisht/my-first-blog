# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
from .models import Post

admin.site.register(Post)#To make our model visible on the admin page,
# we need to register the model with admin.site.register(Post).


# Register your models here.
