from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'login_form.html')


def mainpage(request):
    return render(request, 'mainpage.html')
