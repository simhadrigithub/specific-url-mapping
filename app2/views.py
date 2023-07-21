from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("<marquee><i>THIS IS MY SECOND APP2</i></marquee>")