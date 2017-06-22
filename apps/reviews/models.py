# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def post(self, data):
        errors = []
        if len(data['author']) <1:
            author=data['authorlist']
        else:
            author=data['author']
        if len(data['title'])<1:
            errors.append('Title can not be blank')
            print "error 1"
            pass
        if len(data['review'])< 1:
            errors.append('Review can not be blank') 
            print "error2"
            pass
        if errors:
            return {'errors':errors}
        if not Book.objects.filter(title=data['title']).exists():
            return {'book': "new"}
        if Author.objects.filter(name=data['author']).exists():
            return {}
        else:
            return {'author':author}  

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.CharField(max_length=500)
    review_user = models.ForeignKey('login.User',related_name="reviews" )
    star = models.SmallIntegerField()
    review_book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
