from projects import views
from django.urls import path


urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_details, name='project_details')
]