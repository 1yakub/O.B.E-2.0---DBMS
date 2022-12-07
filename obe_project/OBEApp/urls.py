from django.urls import path
from . import views
urlpatterns =[ 
    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('question', views.question, name="question"),
    path('course', views.course, name="course"),

]