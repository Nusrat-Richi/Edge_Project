import os
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serialize import ProductsSerializers
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import Product 
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdmin,isStaff
from rest_framework.permissions import IsAuthenticated

from django_auth.settings import BASE_DIR
def index(request):
    return HttpResponse("Hello, world. You're at the product index.")

p = os.path.join(BASE_DIR,"templates")

def signup(request):
    return render(request,"signup.html")
def login(request):
    return render(request,"login.html") 
def home(request):
    return render(request,"home.html")