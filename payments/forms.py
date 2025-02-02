from django import forms
from django.forms import ModelForm
from .models import *



class Payment_MF(ModelForm):
	class Meta:
		model = Payment
		fields = "__all__"


class Invoice_MF(ModelForm):
	class Meta:
		model = Invoice
		fields = "__all__"


class Payout_MF(ModelForm):
	class Meta:
		model = Payout
		fields = "__all__"
