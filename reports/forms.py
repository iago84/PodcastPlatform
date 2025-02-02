from django import forms
from django.forms import ModelForm
from .models import *



class Report_MF(ModelForm):
	class Meta:
		model = Report
		fields = "__all__"


class FlaggedContent_MF(ModelForm):
	class Meta:
		model = FlaggedContent
		fields = "__all__"
