from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
# from django.contrib import auth
from shop.models import Contact


def homepage1(request):
    return render(request, 'shop/homepage.html')
