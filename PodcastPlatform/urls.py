"""
URL configuration for PodcastPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
import podcast.urls as podcast_urls

# Automatically added app include
urlpatterns.append(path('', include(podcast_urls)))
import subscriptions.urls as subscriptions_urls

# Automatically added app include
urlpatterns.append(path('', include(subscriptions_urls)))
import calls.urls as calls_urls

# Automatically added app include
urlpatterns.append(path('', include(calls_urls)))
import users.urls as users_urls

# Automatically added app include
urlpatterns.append(path('', include(users_urls)))
import payments.urls as payments_urls

# Automatically added app include
urlpatterns.append(path('', include(payments_urls)))
import reports.urls as reports_urls

# Automatically added app include
urlpatterns.append(path('', include(reports_urls)))
import recommendations.urls as recommendations_urls

# Automatically added app include
urlpatterns.append(path('', include(recommendations_urls)))
import user_management.urls as user_management_urls

# Automatically added app include
urlpatterns.append(path('', include(user_management_urls)))
import policies_app.urls as policies_app_urls

# Automatically added app include
urlpatterns.append(path('', include(policies_app_urls)))
