"""
wiki/encyclopedia URL Configuration
Created by Agnes Admiraal
in Visual Studio Code WSL: Ubuntu-20.04

The `urlpatterns` list routes URLs to views. 
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name = "title"),
    path("search", views.search, name = "search"),
    path("newpage", views.newpage, name = "newpage"),
    path("error", views.search, name = "error"),                    
    path("randomchoice", views.randomchoice, name = "randomchoice"),       
    path("editpage/<str:title>", views.editpage, name = "editpage")                
]
