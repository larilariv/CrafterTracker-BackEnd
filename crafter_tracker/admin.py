from django.contrib import admin
from .models import Project, Image, Resource

# Register your models here.
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Resource)