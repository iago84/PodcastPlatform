from django.urls import path
from . import views

urlpatterns = [
	path('cookies/', views.cookie_policy, name='cookie_policy'),
	path('legal/', views.legal_advise, name='legal_advise'),
	path('terms/', views.terms_and_conditions, name='terms_and_conditions'),
	path('privacy/', views.privacy_policy, name='privacy_policy'),
]
