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
    def get(self, request, pk, user):
        projects = Project.objects.get(id=pk)
        user = Project.objects.get_username(user)
        serializer = ProjectSerializer(projects, many=False)
        return Response(serializer.data)

class ProjectsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProject(request, pk):
    user = request.user
    project = user.project_set.get(pk=pk)
    project.delete()
    return Response('Project deleted!')





###################################
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.parsers import JSONParser
# from rest_framework.permissions import IsAuthenticated, AllowAny

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# from .serializers import ProjectSerializer
# from crafter_tracker.models import Project

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token',
#         '/api/token/refresh'
#     ]
#     return Response(routes)

# # PUBLIC VIEWS
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def getPublicProjects(request):
#     projects = Project.objects.all()
#     serializer = ProjectSerializer(projects, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def getPublicProjectDetails(request, pk):
#     projects = Project.objects.get(pk=pk)
#     serializer = ProjectSerializer(projects, many=False)
#     return Response(serializer.data)


# # AUTH VIEWS
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def getProjects(request):
#     user = request.user
#     if request.method == 'GET':
#         projects = user.project_set.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         projectdata = JSONParser().parse(request)
#         serializer = ProjectSerializer(data=projectdata)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def getProjectDetails(request, pk):
#     user = request.user
#     try:
#         project = user.project_set.get(pk=pk)
#     except project.DoesNotExist:
#         return Response({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProjectSerializer(project)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         projectdata = JSONParser().parse(request)
#         serializer = ProjectSerializer(project, data=projectdata)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         project.delete()
#         return Response({'message': 'Project was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)