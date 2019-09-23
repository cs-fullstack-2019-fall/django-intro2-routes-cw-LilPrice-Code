from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def allGood(request):
    return HttpResponse("Here you go! Free Games!!!!")

def joy(request):
    return HttpResponse("Stimpy & Ren rocks!")

    # HttpResponse HttpResponse