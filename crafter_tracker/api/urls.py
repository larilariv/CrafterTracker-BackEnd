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
    path('projects/<str:pk>/delete/', views.deleteProject, name="delete-project"),

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