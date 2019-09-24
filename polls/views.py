from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. We are at the polls index.")