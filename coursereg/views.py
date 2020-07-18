from django.shortcuts import render, redirect
from .models import CourseModel
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url = "/accounts/login/")
def course_create(request):
	if request.method == 'POST':
		form  = forms.CourseForm(request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.User = request.user
			instance.save()
			return redirect('coursereg:course_list')
    	
	else:	
	  form = forms.CourseForm()
	return render(request, 'coursereg/course_create.html', {'form': form})


@login_required
def course_list(request):
	
	courses = CourseModel.objects.all().filter(User = request.user).order_by('date')
	return render(request, 'coursereg/course_list.html', {'courses': courses})	