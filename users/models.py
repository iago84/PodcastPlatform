from django.db import models

class UserProfile(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile', verbose_name='User')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='Profile Picture')
    bio = models.TextField(blank=True, null=True, verbose_name='Bio')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone Number')

    def __str__(self):
        return f'Profile - {self.user.username}'

class Role(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Role Name')
    description = models.TextField(blank=True, null=True, verbose_name='Role Description')

    def __str__(self):
        return self.name

class Permission(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Permission Name')
    description = models.TextField(blank=True, null=True, verbose_name='Permission Description')

    def __str__(self):
        return self.name

class Message(models.Model):
    model_state = models.BooleanField(default=True)
    date_created = models.DateTimeField('Date Creation', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Date Update', auto_now=True, auto_now_add=False)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sent_messages', verbose_name='Sender')
    receiver = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='received_messages', verbose_name='Receiver')
    subject = models.CharField(max_length=255, verbose_name='Subject')
    body = models.TextField(verbose_name='Body')
    read = models.BooleanField(default=False, verbose_name='Read')

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'
