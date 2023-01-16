from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import requests
# Create your views here.
class bitcoin(View):
    template_name = "bitcoin.html"
    response = requests.get("https://newsapi.org/v2/everything?q=crypto%20AND%20btc%20AND%20bitcoin%20AND%20ETH%20AND%20xrp&searchIn=title,description&pageSize=10&page=1&apiKey=810d44d02b5c48c797a2f07788ebc367&from=2023-01-13&to=2023-01-13")

  
    def get(self, request):
        return render(request,self.template_name,self.response)   