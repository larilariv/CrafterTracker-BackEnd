from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.GetRoutes.as_view(), name="get_routes" ),

    path('publicprojects/', views.PublicProjectsList.as_view(), name="public_projects_list"),
    path('publicprojects/<str:pk>/', views.PublicProjectDetails.as_view(), name="public-project-detail"),

    path('projects/', views.ProjectsList.as_view(), name="project-list"),
    path('projects/create/', views.ProjectsList.as_view(), name="create-project"),
    path('projects/<str:pk>/', views.ProjectDetails.as_view(), name="project-detail"),
    path('projects/<str:pk>/delete/', views.ProjectDetails.as_view(), name="delete-project"),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
