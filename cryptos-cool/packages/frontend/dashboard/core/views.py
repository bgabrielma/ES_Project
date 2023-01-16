from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Employee
import requests


# class Index(LoginRequiredMixin, View):
class Index(View):
    template = 'index.html'
    login_url = '/login/'
    
    def get(self, request):
        # employees = Employee.objects.all()
        return render(request, self.template)



# class Login(View):
#     template = 'login.html'
    
#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, self.template, {'form': form})

#     def post(self, request):
#         form = AuthenticationForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, self.template, {'form': form})
