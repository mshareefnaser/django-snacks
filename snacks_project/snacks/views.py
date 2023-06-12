from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return HttpResponse('<h1>Snacks Home</h1>')

def about(request):
    return HttpResponse('<h1>Snacks About</h1>')