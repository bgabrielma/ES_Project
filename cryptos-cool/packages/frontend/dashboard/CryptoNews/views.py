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
        self.template_name = "News.html"
        response = requests.get("https://newsapi.org/v2/everything?q=crypto%20AND%20btc%20AND%20bitcoin%20AND%20ETH%20AND%20xrp&searchIn=title,description&pageSize=10&page=1&apiKey=810d44d02b5c48c797a2f07788ebc367&from=2023-01-13&to=2023-01-13")
        self.response = response.json()
        dict = {'title': [self.response["articles"][0]["title"]],
                'description' :  [self.response["articles"][0]["description"]],
                 'content': [self.response["articles"][0]["content"]]}
        self.context = self.checkall(dict)
        self.dict2 = {"news" : dict}
        print(self.dict2)
        # print(response["articles"])
    
    def get(self, request):
        return render(request,self.template_name,self.dict2)   
    
    def checkall(self,dict):

        for k in range(1, self.response["totalResults"]):
            dict["title"].append(self.response["articles"][k]["title"])  
            dict["description"].append(self.response["articles"][k]["description"])  
            dict["content"].append(self.response["articles"][k]["content"])  
        return dict
