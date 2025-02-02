from django import forms
from django.forms import ModelForm
from .models import *



class Recommendation_MF(ModelForm):
	class Meta:
		model = Recommendation
		fields = "__all__"


class Algorithm_MF(ModelForm):
	class Meta:
		model = Algorithm
		fields = "__all__"
