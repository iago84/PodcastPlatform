from django.db import models

class Recommendation(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=200, verbose_name='Recommendation Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    user_rating = models.FloatField(default=0.0, verbose_name='User Rating')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    def __str__(self):
        return f'Recommendation - {self.name}'

class Algorithm(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=200, verbose_name='Algorithm Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    version = models.CharField(max_length=50, verbose_name='Version')
    last_run = models.DateTimeField('Last Run', auto_now=False, blank=True, null=True)

    def __str__(self):
        return f'Algorithm - {self.name}'
