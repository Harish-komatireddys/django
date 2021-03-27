from . import views
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("oauth/", include("social_django.urls")),
    path('register/', views.register, name='register')
]