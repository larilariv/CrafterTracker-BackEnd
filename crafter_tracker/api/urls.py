from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('allprojects/', views.getAllProjects, name="public-project-list"),
    path('allprojects/<int:pk>/', views.getAllProjectDetails, name="public-project-detail"),
    path('projects/', views.getProjects, name="project-list"),
    path('projects/create/', views.createProject, name="create-project"),
    path('projects/<int:pk>/', views.getProjectDetails, name="project-detail"),
    path('projects/<int:pk>/delete/', views.deleteProject, name="delete-project"),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]





##############################
# from django.urls import path
# from . import views
# from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('', views.getRoutes),
#     path('projects/', views.getProjects, name="project-list"),
#     path('projects/<int:pk>/', views.getProjectDetails, name="project-detail"),
#     path('public/projects/', views.getPublicProjects, name="public-project-list"),
#     path('public/projects/<int:pk>/', views.getPublicProjectDetails, name="public-project-detail"),

#     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]