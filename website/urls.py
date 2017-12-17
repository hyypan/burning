# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin

from  apis.articles import *


urlpatterns = [
    url(r'^articles/$', articles)
]
