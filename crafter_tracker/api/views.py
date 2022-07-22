from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProjectSerializer
from crafter_tracker.models import Project

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllProjectDetails(request, pk):
    projects = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    user = request.user
    projects = user.project_set.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjectDetails(request, pk):
    user = request.user
    projects = user.project_set.get(pk=pk)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProject(request):
    data = request.data
    project = Project.objects.create(
        name=data['name'],
        description=data['description'],
    )
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)










# @api_view(['GET'])
# @permission_classes([AllowAny])
# def getProjects(request):
#     print("I'm in projects")
#     print(type(request.user))
    # if request.user == 'AnonymousUser':
    # if True:
    #     results = Project.objects.all()
    #     print(results)
    #     return Response(results)

    # user = request.user
    # projects = user.project_set.all()
    # serializer = ProjectSerializer(projects, many=True)
    # return Response(serializer.data)