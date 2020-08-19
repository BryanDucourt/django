from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from login import login as func

def mainpage(request):
    return render(request, 'mainpage.html')

@csrf_exempt
# Create your views here.
def login(request):
    resp = func.login(request)
    return HttpResponse(resp)


@csrf_exempt
def register(request):
    resp = func.register(request)
    return HttpResponse(resp)
