#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import patterns,url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register', views.register, name='register'),
    url(r'^about/$', views.about, name='about'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'add_category/$', views.add_category, name='add_category'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'login/$', views.user_login, name='login'),
]
