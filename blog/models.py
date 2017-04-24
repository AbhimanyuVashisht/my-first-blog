# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.utils import timezone

class Post(models.Model): #models.Model means that the Post is a Django model,
    #  so Django knows that it should be stored in the database
    # defining the properties like author, title ,text

    author = models.ForeignKey('auth.User')# to link another model
    title = models.CharField(max_length=200)# text with limited no. of characters
    text = models.TextField()# long text without any limit
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # return the title of the blog
    def __str__(self):
        return self.title


# Create your models here.
