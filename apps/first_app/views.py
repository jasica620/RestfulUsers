from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
	context = { "user" : User.objects.all()}
	return render(request, "restful.html", context)

def new(request):
	return render(request,'newUser.html')

def edit(request, id):
	context = {"user": User.objects.get(id=id)}
	return render(request,'edit.html', context)

def show(request, id):
	context = {"user": User.objects.get(id=id)}
	return render(request,"showUser.html", context)

def create(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for key, value in errors.items():
				messages.error(request, value)
			return redirect('/users/new')
		else:
			user = User.objects.create()
			user.first_name = request.POST['first_name']
			user.last_name = request.POST['last_name']
			user.email = request.POST['email']
			user.save()
			return redirect('/')

def destroy(request, id):
	User.objects.get(id=id).delete()
	return redirect('/')

def update(request, id):
	if request.method == "POST":
		user = User.objects.get(id=id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
	return redirect(reverse('show', kwargs={'id': id}))