# Generated by Django 4.2.13 on 2025-02-02 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Update')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Permission Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Permission Description')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Update')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Role Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Role Description')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Update')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/', verbose_name='Profile Picture')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Update')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='Receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
        ),
    ]
