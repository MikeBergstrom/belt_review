from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books),
    url(r'add$', views.add),
    url(r'process$', views.process),
    url(r'^books/(?P<id>\d+)$', views.book, name= "show_book"),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^home$', views.books),
    url(r'^delete/(?P<bookid>\d+)/(?P<reviewid>\d+)$', views.delete),
    url(r'^logout$', views.logout)

]