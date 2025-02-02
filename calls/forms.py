from django import forms
from django.forms import ModelForm
from .models import *



class Call_MF(ModelForm):
	class Meta:
		model = Call
		fields = "__all__"


class VideoCall_MF(ModelForm):
	class Meta:
		model = VideoCall
		fields = "__all__"


class CallHistory_MF(ModelForm):
	class Meta:
		model = CallHistory
		fields = "__all__"
