from django import forms
from django.forms import CharField
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'id': 'name', })
		self.fields['password1'].widget.attrs.update({'id': 'p1', })
		self.fields['password2'].widget.attrs.update({'id': 'p2', })