from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
from time import sleep
import asyncio

class BussinessLogic:
	@staticmethod
	async def update_models():
		url_models = UrlModel.objects.filter(check=True)
		for url_model in url_models:
			try:
				status = True if requests.get(url_model.url).status_code == 200 else False
			except:
				status = False
			url_model.url_status = status
			url_model.save()
