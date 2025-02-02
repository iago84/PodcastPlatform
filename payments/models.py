from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
	model_state = models.BooleanField(default=True, verbose_name=_("Model State"))
	date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Creation"))
	date_modified = models.DateTimeField(auto_now=True, verbose_name=_("Date Update"))

	class Meta:
		abstract = True


class Payment(BaseModel):
	amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
	method = models.CharField(max_length=50, choices=[("Credit Card", "Credit Card"), ("PayPal", "PayPal"),
	                                                  ("Bank Transfer", "Bank Transfer")], default="Credit Card")
	status = models.CharField(max_length=50,
	                          choices=[("Pending", "Pending"), ("Completed", "Completed"), ("Failed", "Failed")],
	                          default="Pending")

	def __str__(self):
		return f"Payment of {self.amount} via {self.method} ({self.status})"


class Invoice(BaseModel):
	number = models.CharField(max_length=100, unique=True, verbose_name=_("Invoice Number"))
	payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name="invoices")
	total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Amount"))
	paid = models.BooleanField(default=False, verbose_name=_("Paid"))

	def __str__(self):
		return f"Invoice {self.number} - {'Paid' if self.paid else 'Unpaid'}"


class Payout(BaseModel):
	recipient = models.CharField(max_length=255, verbose_name=_("Recipient"))
	amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
	status = models.CharField(max_length=50,
	                          choices=[("Pending", "Pending"), ("Completed", "Completed"), ("Failed", "Failed")],
	                          default="Pending")

	def __str__(self):
		return f"Payout to {self.recipient} of {self.amount} ({self.status})"



