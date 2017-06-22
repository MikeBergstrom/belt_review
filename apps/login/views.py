# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import datetime


def index(request):
    # User.objects.all().delete()
    return render(request, 'login/index.html')

def login(request):
    user= User.objects.login(request.POST)
    if user['status']:
        request.session['first'] = user['user'].first_name
        request.session['id'] = user['user'].id
        request.session['status'] = "logged in"
        return redirect('/books')
    else:
        for error in user['errors']:
            messages.error(request, error, extra_tags="login")
        return redirect('/')

def register(request):
    print "in register"
    user = User.objects.register(request.POST)
    print user
    if not user['status']:
        for error in user['errors']:
            messages.error(request, error, extra_tags="register")
        return redirect ('/')
    else:
        print "register success"
        print user['user'].first_name
        request.session['first'] = user['user'].first_name
        request.session['id'] = user['user'].id
        print request.session['first']
        print request.session['id']
        return redirect ('/books')    
