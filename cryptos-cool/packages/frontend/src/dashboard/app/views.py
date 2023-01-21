from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import requests
import json

class News(View):
    def __init__(self):
        self.template_name = "news.html" 

    def get(self, request):
        data = dict()
        page = request.GET.get('page', "1")
        
        data = requests.get(f"http://host.docker.internal:2000/api/news?search=crypto%20AND%20xrp%20AND%20btc&page={page}").json()
        if (data.get("error")):
            data = dict()

        return render(request, self.template_name, {
            "news": data.get("articles", dict()),
            "total_pages": data.get("pages", 0),
            "current_page": page,
        })

class Coins(View):
    def __init__(self):
        self.template_name = "coins.html"

    def get(self, request):
        coin = "BTC"
        
        data = requests.get(f"http://host.docker.internal:2000/api/coins?type={coin}&days=14").json()

        if (data.get("error")):
            data = dict()

        minimum = float(min(data.get("data")[0]))
        maximum = float(max(data.get("data")[0]))
        
        return render(request, self.template_name, {
            "data": data,
            "coin": coin,
            "minimum": f"{minimum:0.4f}",
            "maximum": f"{maximum:0.4f}"
        })