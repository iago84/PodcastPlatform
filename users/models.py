from django.db import models

# Create your models here.


class UserProfile(models.Model):
	model_state = models.BooleanField(default=True)
	date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)


class Role(models.Model):
	model_state = models.BooleanField(default=True)
	date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)


class Permission(models.Model):
	model_state = models.BooleanField(default=True)
	date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)


class Message(models.Model):
	model_state = models.BooleanField(default=True)
	date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
