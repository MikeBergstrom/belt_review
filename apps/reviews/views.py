# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Author
from .models import Book
from .models import Review
from ..login.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count

# Create your views here.
def books(request):
    books = Book.objects.all()
    print books
    reviews= Review.objects.order_by('-created_at')[:3]
    context = {
        'reviews':reviews,
        'books':books
    }
    print reviews
    return render(request, 'reviews/books.html', context)

def add(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'reviews/add.html', context)

def process(request):
    review = Review.objects.post(request.POST)
    author = request.POST['authorlist']
    print request.POST['title']
    if 'errors' in review:
        print "errors"
        print review['errors']
        for error in review['errors']:
            messages.error(request, error)
        return redirect('/add')
    if 'author' in review:
        print review['author']
        print "second"
        author = request.POST['author']
        Author.objects.create(name=request.POST['author'])
        pass
    if 'book' in review:
        print "add book"
        Book.objects.create(title=request.POST['title'], book_author=Author.objects.get(name=author))
        pass

    print "third"
    print request.POST['title']
    stars = int(request.POST['stars'])
    # Book.objects.create(title=request.POST['title'], book_author=Author.objects.get(name=request.POST['author']))
    Review.objects.create(review=request.POST['review'], review_user=User.objects.get(id=request.session['id']), star=stars, review_book=Book.objects.get(title=request.POST['title']))
    thisbook = Book.objects.get(title=request.POST['title'])
    print thisbook
    id = thisbook.id
    print thisbook.id
    return redirect (reverse('show_book', kwargs={'id':id}))

def book(request, id):
    print id
    print "in book"
    book = Book.objects.get(id=id)
    print book.title
    reviews = Review.objects.filter(review_book__id=id)
    author = Author.objects.get(book__id=id)
    context = {'book':book, 'reviews' : reviews, 'author':author}
    return render(request, 'reviews/showbook.html', context)

def user(request, id):
    user = User.objects.annotate(total_reviews=Count('reviews')).get(id=id)
    reviews = Review.objects.filter(review_user__id=id)[:3]
    
    context = {
        'user':user,
        'reviews':reviews
    }
    return render(request, 'reviews/user.html', context)

def delete(request, bookid, reviewid):
    Review.objects.get(id=reviewid).delete()
    return redirect(reverse('show_book', kwargs={'id':bookid}))

def logout(request):
    request.session['first'] = None
    request.session['id'] = None
    return redirect ('/')