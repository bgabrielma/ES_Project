from http.client import HTTPResponse
from django.contrib import admin
from django.urls import path,include
from . import views
from django.http import HttpRequest
from django.views.generic import TemplateView

urlpatterns = [
    path('',  views.bitcoin.as_view(), name='bitcoin')
]