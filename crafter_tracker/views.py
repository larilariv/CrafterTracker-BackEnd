from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from .models import Project, Image, Resource, Material

# drf related imports
from rest_framework import generics
from .serializers import ProjectSerializer, ImageSerializer, ResourceSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer