from django import forms
from django.forms import ModelForm
from .models import *



class Plan_MF(ModelForm):
	class Meta:
		model = Plan
		fields = "__all__"


class Subscription_MF(ModelForm):
	class Meta:
		model = Subscription
		fields = "__all__"


class Transaction_MF(ModelForm):
	class Meta:
		model = Transaction
		fields = "__all__"
