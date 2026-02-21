from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<h2>Hello Webprog IT242 world!<h2>")