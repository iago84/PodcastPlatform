from django import forms
from django.forms import ModelForm
from .models import *



class Episode_MF(ModelForm):
	class Meta:
		model = Episode
		fields = "__all__"


class Category_MF(ModelForm):
	class Meta:
		model = Category
		fields = "__all__"


class Statistic_MF(ModelForm):
	class Meta:
		model = Statistic
		fields = "__all__"


class Comment_MF(ModelForm):
	class Meta:
		model = Comment
		fields = "__all__"


class Download_MF(ModelForm):
	class Meta:
		model = Download
		fields = "__all__"
