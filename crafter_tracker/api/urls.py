from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('allprojects/', views.getAllProjects),
    path('allprojects/<int:pk>/', views.getAllProjectDetails),
    path('projects/', views.getProjects),
    path('projects/<int:pk>/', views.getProjectDetails),
    path('projects/create', views.createProject),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]