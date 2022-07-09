from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.

from .models import Project, Image, Resource, Material

# drf related imports
from rest_framework import generics
from .serializers import ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer