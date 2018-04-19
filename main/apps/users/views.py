# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bcrypt import hashpw, gensalt
from django.shortcuts import render, redirect, HttpResponse
from models import User

# Create your views here.

def index(request):
	return render(request, "users/index.html")

def register(request):
	if request.POST:
		salt = gensalt()
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], salt=salt, pw=hashpw(request.POST['password'].encode(), salt))
	return redirect(index)

def login(request):
	pw1 = User.objects.get(email=request.POST['email']).pw
	pw2 = hashpw(request.POST['password'].encode(), User.objects.get(email=request.POST['email']).salt.encode())
	if pw1 == pw2:
		return HttpResponse("Logged in")
	else:
		return HttpResponse("Something is wrong")