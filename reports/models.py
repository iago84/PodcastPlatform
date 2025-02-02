from django.db import models

class Report(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=200, verbose_name='Report Title')
    content = models.TextField(verbose_name='Report Content')
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed'), ('in_progress', 'In Progress')], default='open', verbose_name='Status')

    def __str__(self):
        return f'Report - {self.title}'

class FlaggedContent(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    content_type = models.CharField(max_length=50, choices=[('image', 'Image'), ('video', 'Video'), ('text', 'Text')], verbose_name='Content Type')
    content_description = models.TextField(blank=True, null=True, verbose_name='Content Description')
    flagged_by = models.CharField(max_length=100, verbose_name='Flagged By')

    def __str__(self):
        return f'Flagged Content - {self.content_type}'
