from django.contrib import admin

# Register your models here.
from .models import Episode
from .models import Category
from .models import Statistic
from .models import Comment
from .models import Download

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_created', 'model_state')
	search_fields = ('title',)
	list_filter = ('date_created',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_created', 'model_state')
	search_fields = ('name',)
	list_filter = ('date_created',)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
	list_display = ('episode', 'views', 'likes', 'date_created', 'model_state')
	search_fields = ('episode__title',)
	list_filter = ('date_created',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('episode', 'author', 'date_created', 'model_state')
	search_fields = ('author', 'episode__title')
	list_filter = ('date_created',)


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
	list_display = ('episode', 'file_url', 'date_created', 'model_state')
	search_fields = ('episode__title',)
	list_filter = ('date_created',)
