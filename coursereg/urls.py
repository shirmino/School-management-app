from django.urls import path

from . import views

app_name = 'coursereg'

urlpatterns = [
    path('create/', views.course_create, name='course_create'),
    path('', views.course_list, name='course_list'),
      
]