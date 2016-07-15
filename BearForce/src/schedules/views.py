from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from .models import User, News_Messages, Shift

# Create your views here.

def index(request):
	bearforce_worker = User.objects.get(pk=1)
	shifts_to_work = bearforce_worker.shift_set.all()
	bearforce_messages = News_Messages.objects.all()
	context= {
		"shifts_to_work": shifts_to_work,
		"bearforce_worker": bearforce_worker,
		"bearforce_messages": bearforce_messages,
	}
	#get_object_or_404
	return render(request, 'schedules/index.html', context)

def new_message(request):
	return HttpResponse("Hello, new message view is working.")
	
def shift_pick_up(request):
	return HttpResponse("Hello, shift pickup view is working.")

def shift_release(request):
	return HttpResponse("Hello, shift release view is working.")

def staff(request):
	return HttpResponse("Hello, staff view is working.")

def account(request, user_id):
	return HttpResponse("Hello, account view is wokring.")