from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

# Create your views here.

def index(request):
	return HttpResponse("Hello, Views is working.")

def shift_pick_up_view(request):
	return HttpResponse("Hello, shift pickup view is working.")

def shift_release_view(request):
	return HttpResponse("Hello, shift release view is working.")

def staff_view(request):
	return HttpResponse("Hello, staff view is working.")

def account_view(request):
	return HttpResponse("Hello, account view is wokring.")