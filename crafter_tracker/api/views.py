from django.http import JsonResponse

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProjectSerializer
from crafter_tracker.models import Project

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class GetRoutes(APIView):
    def get(self, request):
        routes = [
        '/api/token',
        '/api/token/refresh'
    ]
        return Response(routes)

class PublicProjectsList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class PublicProjectDetails(APIView):
    def get(self, request, pk):
        projects = Project.objects.get(id=pk)
        # user = Project.objects.get_username(user)
        serializer = ProjectSerializer(projects, many=False)
        return Response(serializer.data)

class ProjectsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        projects = user.project_set.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        project = Project.objects.create(
            name=data['name'],
            description=data['description'],
            user = request.user
        )
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)

class ProjectDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user
        project = user.project_set.get(id=pk)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = request.user
        project = user.project_set.get(id=pk)
        project.delete()
        return Response('Project deleted!')

