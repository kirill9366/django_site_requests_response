from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', IndexView.as_view()),
    path('urlresponse', UrlResponse.as_view()),
]