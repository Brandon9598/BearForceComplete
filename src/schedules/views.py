from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from .models import User, News_Messages, Shift

# Create your views here.

def home(request):
	latest_mn = News_Messages.objects.all()
	output = "***".join(nm.title for nm in latest_mn)
	return HttpResponse(output)

def shift_pick_up(request):
	return HttpResponse("Hello, shift pickup view is working.")

def shift_release(request):
	return HttpResponse("Hello, shift release view is working.")

def staff(request):
	return HttpResponse("Hello, staff view is working.")

def account(request, user_id):
	return HttpResponse("Hello, account view is wokring.")