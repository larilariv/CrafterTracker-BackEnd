from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    complete = models.BooleanField()
    images = models.ImageField(upload_to ='uploads/')
    materials = models.CharField(max_length=50)
    resources = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.name