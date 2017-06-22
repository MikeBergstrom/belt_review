# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import datetime


def index(request):
    timediff = (datetime.datetime.now()-datetime.datetime.now())
    # print timediff.total_minutes()
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
    # if 'useremail' in user:
    #     print "success"
    #     request.session['first']=request.POST['first']
    #     request.session['status']="registered"
    #     User.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=request.POST['password'])
    #     getid = User.objects.get(email=request.POST['email'])
    #     request.session['id'] = getid.id
    #     return redirect('/books')
    # elif 'errors' in user:
    #     request.session['errors']=user['errors'][0]
    #     print "failure"
    #     print user['errors']
    #     for error in user['errors']:
    #         messages.error(request, error, extra_tags="register")
    #     return redirect('/')
    
