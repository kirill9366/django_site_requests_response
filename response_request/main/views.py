from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
import requests
from celery import Celery
# from .services import BussinessLogic

# logic = BussinessLogic()

class IndexView(TemplateView):

	html_template = "main/main.html"
	def dispatch(self, request, *args, **kwargs):
		url_models = UrlModel.objects.all()
		interval = 9
		return render(request, self.html_template, {'url_models': url_models, 'interval': interval})

class UrlResponse(APIView):
	permission_classes = [AllowAny]
	def dispatch(self, request,  *args, **kwargs):
		if request.method == "POST":
			context = {'urls': []}
			url_models = UrlModel.objects.all()
			for url_model in url_models:
				context['urls'].append({'id':url_model.id,'status':url_model.url_status})
			return JsonResponse(context)