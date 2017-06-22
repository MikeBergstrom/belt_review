# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import datetime
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile('^[^0-9]+$')



class UserManager(models.Manager):
    def register(self, data):
        results = {'status':True, 'errors':[], 'user':None}
        print "model register"
        print data['first']
        # month, day, year = map(int, data['birth'].split('/'))
        # print year
        # print month
        # print day
        # print datetime.date.today()
        # print datetime.date(year, month, day)
        if not data['first'] or len(data['first']) < 1:
            results['errors'].append('First name must be at least 2 characters')
            results['status']= False
        if not data['last'] or len(data['last']) < 1:
            results['errors'].append('Last name must be at least 2 characters')
            results['status'] = False
        if not NAME_REGEX.match(data['first']):
            results['errors'].append('First name must be letters only')
            results['status'] = False
        if not NAME_REGEX.match(data['last']):
            results['errors'].append('Last name must be letters only')
            results['status'] = False
        if not EMAIL_REGEX.match(data['email']):
            results['errors'].append('Email not in valid format')
            results['status'] = False
        # if datetime.date(year, month, day) >= datetime.date.today():
        #     errors.append('Birth date must be in the past')
        #     pass
        if data['password'] != data['confirm']:
            results['errors'].append('Passwords do not match')
            results['status'] = False
        if len(data['password']) < 8:
            results['errors'].append('Password must be at least 8 characters')
            results['status'] = False
        if User.objects.filter(email=data['email']).exists():
            results['errors'].append('This email is already registered')
            results['status'] = False
        if results['status']:
            password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            print "successful register"
            user = User.objects.create(first_name=data['first'], last_name=['last'], email=data['email'], password=password)
            user.save()
            results['user'] = user
            print results
        return results


    def login(self, data):
        results = {'status': True, 'errors':[], 'user': None}
        if not User.objects.filter(email=data['email']).exists():
            results['errors'].append('Email is not recognized')
            results['status'] = False
        else:
            user = User.objects.get(email=data['email'])
            if not bcrypt.hashpw(data['password'].encode(), user.password.encode()):
                print "bad password"
                results['errors'].append('Incorrect Password')
            else:
                results['user'] = user
                print user
                return results

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
