from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('thanks/', views.thanks, name='thanks')
    
]