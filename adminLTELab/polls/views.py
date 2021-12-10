"""
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'polls/index.html')

def profile(request):
    return render(request, 'polls/profile.html')