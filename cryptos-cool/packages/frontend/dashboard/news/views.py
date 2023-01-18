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
        response = requests.get("http://localhost:8000/news?q=crypto%20AND%20btc%20AND%20bitcoin%20AND%20ETH%20AND%20xrp&searchIn=title,description&pageSize=10&page=1&apiKey=810d44d02b5c48c797a2f07788ebc367&from=2023-01-13&to=2023-01-13")
        self.response = response.json()
    
    def get(self, request):
        return render(request, self.template_name, {
            "news": self.response["articles"]
        })   
    
    def checkall(self,dict):

        for k in range(1, self.response["totalResults"]):
            dict["title"].append(self.response["articles"][k]["title"])  
            dict["description"].append(self.response["articles"][k]["description"])  
            dict["content"].append(self.response["articles"][k]["content"])  
        return dict
    def pagination(self):
        pags = self.response["totalResults"] / 10
        if pags >= 10:
            pags= 10
            return pags
        else:
            return pags
