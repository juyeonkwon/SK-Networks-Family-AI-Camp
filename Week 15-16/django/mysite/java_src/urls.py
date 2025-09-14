from django.urls import path
from java_src import views

app_name = 'java_src'

urlpatterns = [
    path("", views.index),
]