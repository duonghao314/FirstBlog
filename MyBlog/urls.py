from django.urls import path, include
from django.conf.urls import url
from MyBlog import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('/index',views.index, name = 'index'),
    url(r'^(?P<catName>[a-z]+)/$', views.cat, name='cat'),
    url(r'^article/(?P<artID>[0-9]+)/$', views.art, name='art'),
]