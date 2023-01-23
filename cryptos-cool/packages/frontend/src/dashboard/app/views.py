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
from datetime import timedelta

coins_dataset = [{"BTC": "Bitcoin"},{"ETH": "Etherium"},{"XRP": "Ripple"}]
class News(View):
    # Espécie de "state"
    current_coins_filters = []
    current_news_from_date = None

    def __init__(self):
        self.template_name = "news.html"

    def update_current_coins_filters(self, request):
        self.current_coins_filters.clear()
        
        for coins in coins_dataset:
            for key, _ in coins.items():
                option_value = request.GET.get(f"option_search_coin_{key}", None)
                if option_value is not None:
                    self.current_coins_filters.append(option_value)

        # Se não vier nenhuma das options, ativar todas as moedas
        if (len(self.current_coins_filters) == 0):
            for coins in coins_dataset:
                for key, _ in coins.items():
                    self.current_coins_filters.append(key)
                    
    def update_from_date(self, request):
        # format YYYY-MM-DD
        self.current_news_from_date = request.GET.get('from_date', (datetime.datetime.now() - timedelta(weeks=4.34812141)).strftime('%Y-%m-%d')) # meter default para 30 dias
                    
    def get(self, request):
        data = dict()
        page = request.GET.get('page', "1")
    
        self.update_current_coins_filters(request)
        self.update_from_date(request)

        search_query = ""
        for coin in self.current_coins_filters:
            search_query += coin
            if coin != self.current_coins_filters[len(self.current_coins_filters) - 1]:
                search_query += "%20OR%20"

        url = f"http://host.docker.internal:2000/api/news?search={search_query}&page={page}&from_date={self.current_news_from_date}"
        data = requests.get(url).json()
        # "articles": 
        # "pages": 
        # "total_results":
        newsdivided = {}
        page = 1
        number_of_items_per_page = 0
        for news in data["articles"]:
            
            newsdivided["page_{page}"].update(news)
            number_of_items_per_page += 1
            if number_of_items_per_page >= 10:
                number_of_items_per_page = 0
                page += 1
           
        if (data.get("error")):
            data = dict()

        return render(request, self.template_name, {
            "news": data.get("articles", dict()),
            "total_pages": data.get("pages", 0),
            "current_page": page,
            "search": search_query,
            "coins": coins_dataset,
            "current_coins_filters": self.current_coins_filters,
            "current_date": datetime.datetime.now().strftime('%Y-%m-%d'),
            "max_minimum_date": (datetime.datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
            "api_news_url": url
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
            "coins": coins_dataset
        })