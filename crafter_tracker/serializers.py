from rest_framework import serializers
from .models import Project, Image, Resource, Material

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        view_name='image_detail',
        many=True,
        read_only=True
    )
    # resources = serializers.HyperlinkedRelatedField(
    #     view_name='resource_detail',
    #     many=True,
    #     read_only=True
    # )
    # materials = serializers.HyperlinkedRelatedField(
    #     view_name='material_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Project
        fields = ('id', 'name', 'category', 'complete', 'start_date', 'end_date', 'notes', 'images')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'images')