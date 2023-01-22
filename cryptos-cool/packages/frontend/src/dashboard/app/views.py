from datetime import datetime
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
import datetime

class News(View):
    def __init__(self):
        self.template_name = "news.html" 

    def concat(self, words, sep = "%20AND%20"):
      
        for word in words:  
            if word == "None":
                words.remove(word)

        value = sep.join(words)

        return value
    def get(self, request):
        data = dict()
        page = request.GET.get('page', "1")
        start = request.GET.get('start', datetime.datetime.now().strftime('%Y-%m-%d'))
        end = request.GET.get('end', datetime.datetime.now().strftime('%Y-%m-%d'))
        bitcoin = request.GET.get('btc', None)
        ripple = request.GET.get('xrp', None)
        etherium = request.GET.get('eth', None)

        # start = datetime.datetime(start)
        # start.strftime('%Y-%m-%d')
        # end = datetime.datetime(end)
        # end.strftime('%Y-%m-%d')
    
        if bitcoin is None and ripple is None and etherium is None:
            search = "BTC"
        else:
            search = self.concat([str(bitcoin),str(ripple),str(etherium)])
          
      
        data = requests.get(f"http://host.docker.internal:2000/api/news?search={search}&page={page}&from={start}&to={end}").json()
        # data = requests.get(f"http://host.docker.internal:2000/api/news?search=crypto%20AND%20xrp%20AND%20btc&page={page}").json()
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
        

        coin = request.GET.get('type', "BTC")
        days = request.GET.get('days', 14)

        data = requests.get(f"http://host.docker.internal:2000/api/coins?type={coin}&days={days}").json()

        if (data.get("error")):
            data = dict()

        minimum = 0 if len(data) == 0 else float(min(data.get("data")[0]))
        maximum = 0 if len(data) == 0 else  float(max(data.get("data")[0]))
        
        return render(request, self.template_name, {
            "data": data,
            "coin": coin,
            "minimum": f"{minimum:0.4f}",
            "maximum": f"{maximum:0.4f}",
            "coins":  [{"BTC": "Bitcoin"},{"ETH": "Etherium"},{"XRP": "Ripple"}]

        })