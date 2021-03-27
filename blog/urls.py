from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.details, name='details'),
    path('<category>/', views.blog_category, name='blog_category')
]