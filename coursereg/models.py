from django.db import models
from django.contrib.auth.models import User  

# Create your models here.

class CourseModel(models.Model):
    email= models.EmailField(max_length = 30) 
    coursename = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.coursename

    def time(self):
    	return self.duration 