from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import requests

# Create your views here
class news(View):
       
    def __init__(self):
        self.template_name = "news.html" 
    
    def get(self, request):
        data = dict()
        page = request.GET.get('page', "1")
        
        try:
            data = requests.get(f"http://host.docker.internal:2000/api/news?search=crypto%20AND%20xrp%20AND%20btc&page={page}").json()
        except Exception as e:  
            print(f"Failed to load news: {e}")

        return render(request, self.template_name, {
            "news": data.get("articles", dict()),
            "total_pages": data.get("pages", 0),
            "current_page": page,
        })

    def pagination(self):
        pags = self.response["totalResults"] / 10
        if pags >= 10:
            pags= 10
            return pags
        else:
            return pags
