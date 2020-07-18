from . import models
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.CourseModel
        fields = [ 'email','coursename', 'duration']

