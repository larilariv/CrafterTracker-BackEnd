from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    complete = models.BooleanField()
    materials = models.CharField(max_length=50)
    resources = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
    )
    images = models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.name