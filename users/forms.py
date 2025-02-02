from django import forms
from django.forms import ModelForm
from .models import *



class UserProfile_MF(ModelForm):
	class Meta:
		model = UserProfile
		fields = "__all__"


class Role_MF(ModelForm):
	class Meta:
		model = Role
		fields = "__all__"


class Permission_MF(ModelForm):
	class Meta:
		model = Permission
		fields = "__all__"


class Message_MF(ModelForm):
	class Meta:
		model = Message
		fields = "__all__"
