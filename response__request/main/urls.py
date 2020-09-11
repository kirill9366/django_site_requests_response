from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', IndexView.as_view()),
    path('urlresponse', UrlResponse.as_view()),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    ]