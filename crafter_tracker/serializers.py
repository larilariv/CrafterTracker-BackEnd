from rest_framework import serializers
from .models import Project, Image, Resource, Material

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        view_name='image_detail',
        many=True,
        read_only=True
    )
    resources = serializers.HyperlinkedRelatedField(
        view_name='resource_detail',
        many=True,
        read_only=True
    )
    materials = serializers.HyperlinkedRelatedField(
        view_name='material_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Project
        fields = ('id', 'name', 'category', 'complete', 'start_date', 'end_date', 'notes', 'images', 'resources', 'materials')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'images')

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'name', 'link', 'media_type', 'notes')

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'name', 'brand', 'category', 'material_purchase_link', 'notes')