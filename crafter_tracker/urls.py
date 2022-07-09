from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),
    path('images/', views.ImageList.as_view(), name='image_list'),
    path('images/<int:pk>', views.ImageDetail.as_view(), name='image_detail'),
]