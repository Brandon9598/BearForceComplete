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

def messages(request):
	bearforce_messages = News_Messages.objects.all()
	context = {
		"bearforce_messages": bearforce_messages,
	}
	return render(request, 'schedules/messages.html', context)
	
def shift_pick_up(request):
	available_shifts = []
	for shift in Shift.objects.all():
		if (shift.release_shift_temp or shift.release_shift_perm):
			available_shifts.append(shift)
	context = {
		"available_shifts": available_shifts,
	}
	return render(request, 'schedules/pick_up_schedules.html', context)

def shift_release(request):
	bearforce_worker = User.objects.get(pk=1)
	shifts_to_work = bearforce_worker.shift_set.all()
	context = {
		"shifts_to_work": shifts_to_work,
		"bearforce_worker": bearforce_worker,
	}
	return render(request, 'schedules/release_schedules.html', context)

def staff(request):
	return HttpResponse("Hello, staff view is working.")

def account(request, user_id):
	return HttpResponse("Hello, account view is wokring.")