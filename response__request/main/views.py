from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
import requests
from .services import BussinessLogic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,  logout
import asyncio
from .forms import *

logic = BussinessLogic()


class LoginView(TemplateView):
	template_name = "main/loginn.html"

	def dispatch(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)


			if user is not None:
				auth_login(request, user)

				return HttpResponseRedirect('/')
			else:
				context['error'] = "Логин или пароль неправильные"
				form = AuthenticationForm()
				context['form'] = form
				return render(request, self.template_name, context)
		else:
			form = AuthenticationForm()
			context['form'] = form
			return render(request, self.template_name, {'form': form})

class SignUpView(TemplateView):
	template_name = "main/signup.html"

	def dispatch(self, request, *args, **kwargs):

		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				print('i am he')
				user = form.save()
				username = form.cleaned_data.get('username')
				my_password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=my_password)
				auth_login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/signup')
                
		else:
			logout(request)
			form = UserCreationForm()
			return render(request, self.template_name, {'form': form})



class IndexView(TemplateView):

	html_template = "main/main.html"
	def dispatch(self, request, *args, **kwargs):

		if not request.user.is_authenticated:
			return HttpResponse('403 Forbidden')
		url_models = UrlModel.objects.all()

		try:
			interval = IntervalChecksModel.objects.all()[0].interval_second
		except IndexError:
			interval = IntervalChecksModel.objects.create(interval_second=10)
		return render(request, self.html_template, {'url_models': url_models, 'interval': interval})

class UrlResponse(APIView):
	permission_classes = [AllowAny]
	def dispatch(self, request,  *args, **kwargs):

		if request.method == "POST":
			context = {'urls': []}
			logic.update_models()
			url_models = UrlModel.objects.all()
			for url_model in url_models:
				context['urls'].append({'id':url_model.id,'status':url_model.url_status})
			return JsonResponse(context)