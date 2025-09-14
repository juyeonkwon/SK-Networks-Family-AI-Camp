from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.index),
    path('<int:question_id>', views.detail, name='detail'), 
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
]

# http://serv1:8000/board/