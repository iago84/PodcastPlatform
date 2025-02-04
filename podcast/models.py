from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class BaseModel(models.Model):
	model_state = models.BooleanField(default=True, verbose_name=_("Model State"))
	date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Creation"))
	date_modified = models.DateTimeField(auto_now=True, verbose_name=_("Date Update"))

	class Meta:
		abstract = True



class Episode(BaseModel):
	title = models.CharField(max_length=255, verbose_name=_("Title"))
	description = models.TextField(verbose_name=_("Description"))

	def __str__(self):
		return self.title


class Category(BaseModel):
	name = models.CharField(max_length=100, unique=True, verbose_name=_("Category Name"))

	def __str__(self):
		return self.name


class Statistic(BaseModel):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="statistics")
	views = models.PositiveIntegerField(default=0, verbose_name=_("Views"))
	likes = models.PositiveIntegerField(default=0, verbose_name=_("Likes"))

	def __str__(self):
		return f"Stats for {self.episode.title}"


class Comment(BaseModel):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="comments")
	content = models.TextField(verbose_name=_("Comment"))
	author = models.CharField(max_length=100, verbose_name=_("Author"))

	def __str__(self):
		return f"Comment by {self.author}"


class Download(BaseModel):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="downloads")
	file_url = models.URLField(verbose_name=_("Download URL"))

	def __str__(self):
		return f"Download for {self.episode.title}"



