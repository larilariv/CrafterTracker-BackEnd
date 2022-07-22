from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from crafter_tracker.models import Project

class ProjectSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Project
        fields = '__all__'

# from rest_framework import serializers
# from .models import Project, Image, Resource, Material

# class ProjectSerializer(serializers.HyperlinkedModelSerializer):
#     images = serializers.HyperlinkedRelatedField(
#         view_name='image_detail',
#         many=True,
#         read_only=True
#     )
#     resources = serializers.HyperlinkedRelatedField(
#         view_name='resource_detail',
#         many=True,
#         read_only=True
#     )
#     materials = serializers.HyperlinkedRelatedField(
#         view_name='material_detail',
#         many=True,
#         read_only=True
#     )
#     class Meta:
#         model = Project
#         fields = ('user_string', 'name', 'category', 'complete', 'start_date', 'end_date', 'notes', 'images', 'resources', 'materials')

# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Image
#         fields = ('name', 'image')

# class ResourceSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Resource
#         fields = ('name', 'link', 'media_type', 'notes')

# class MaterialSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Material
#         fields = ('projects', 'user_string', 'name', 'brand', 'category', 'purchase_link', 'notes')