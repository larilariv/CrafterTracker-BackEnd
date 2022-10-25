from django.db import models
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField
from traitlets import default

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
        )
    name = models.CharField(max_length=100)
    id = ShortUUIDField(primary_key=True, unique=True, editable=False, length=20, max_length=20, alphabet="abcdefghijklmnopqrstuvwxyz0123456789")
    description = models.CharField(max_length=250)
    categories = models.ManyToManyField('Category', blank=True)
    notes = models.TextField(null=True, blank=True)
    private = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    id = ShortUUIDField(primary_key=True, unique=True, editable=False, length=5, max_length=5, alphabet="0123456789")

    def __str__(self):
        return self.name

# class Image(models.Model):
#     project = models.ForeignKey(
#         Project,
#         on_delete=models.CASCADE,
#         related_name='images',
#     )
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to ='images/')

#     def __str__(self):
#         return self.name

# class Resource(models.Model):
#     project = models.ForeignKey(
#         Project,
#         on_delete=models.CASCADE,
#         related_name='resources',
#     )
#     name = models.CharField(max_length=100)
#     link = models.URLField(max_length=400)
#     media_type = models.CharField(max_length=255)
#     notes = models.TextField()

#     def __str__(self):
#         return self.name

# class Material(models.Model):
#     user = models.ForeignKey(User)
#     projects = models.ManyToManyField(Project)
#     name = models.CharField(max_length=255)
#     brand = models.CharField(max_length=255)
#     category = ArrayField(models.CharField(max_length=255))
#     purchase_link = models.URLField(max_length=400)
#     notes = models.TextField()

#     def __str__(self):
#         return self.name
