from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
	model_state = models.BooleanField(default=True, verbose_name=_("Model State"))
	date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Creation"))
	date_modified = models.DateTimeField(auto_now=True, verbose_name=_("Date Update"))

	class Meta:
		abstract = True


class Call(BaseModel):
	caller = models.CharField(max_length=255, verbose_name=_("Caller"))
	receiver = models.CharField(max_length=255, verbose_name=_("Receiver"))
	duration = models.PositiveIntegerField(help_text=_("Duration in seconds"))

	def __str__(self):
		return f"Call from {self.caller} to {self.receiver}"


class VideoCall(BaseModel):
	caller = models.CharField(max_length=255, verbose_name=_("Caller"))
	receiver = models.CharField(max_length=255, verbose_name=_("Receiver"))
	duration = models.PositiveIntegerField(help_text=_("Duration in seconds"))
	video_quality = models.CharField(max_length=50, choices=[("HD", "HD"), ("SD", "SD"), ("4K", "4K")], default="HD")

	def __str__(self):
		return f"Video Call from {self.caller} to {self.receiver}"


class CallHistory(BaseModel):
	call = models.ForeignKey(Call, on_delete=models.CASCADE, null=True, blank=True)
	video_call = models.ForeignKey(VideoCall, on_delete=models.CASCADE, null=True, blank=True)
	notes = models.TextField(blank=True, verbose_name=_("Notes"))

	def __str__(self):
		return f"History Entry for Call ID {self.call_id or self.video_call_id}"
