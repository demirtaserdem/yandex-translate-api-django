from django.contrib import admin
from django.urls import path
from ytapi import views

app_name = "ytapi"

urlpatterns = [
    path('',views.index,name = "index"),
    path('deleteallsearch',views.deleteAllSearch,name = "deleteAllSearch")
]