from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    complete = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.name

# class ProjectCategory(models.Model):
#     project = models.ForeignKey(
#         Project,
#         on_delete=models.CASCADE,
#         related_name='categories',
#     )
#     cross_stitch = models.BooleanField()
#     crocheting = models.BooleanField()
#     embroidery = models.BooleanField()
#     felting = models.BooleanField()
#     knitting = models.BooleanField()
#     lace_making = models.BooleanField()
#     macrame = models.BooleanField()
#     rug_making = models.BooleanField()
#     sewing = models.BooleanField()
#     shoemaking = models.BooleanField()
#     weaving = models.BooleanField()
#     bookbinding = models.BooleanField()
#     calligraphy = models.BooleanField()
#     cardmaking = models.BooleanField()
#     collage = models.BooleanField()
#     drawing = models.BooleanField()
#     origami = models.BooleanField()
#     painting = models.BooleanField()
#     papier_mache = models.BooleanField()
#     quilling = models.BooleanField()
#     scrapbooking = models.BooleanField()
#     stamping = models.BooleanField()

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

class Resource(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='resources',
    )
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=400)
    media_type = models.CharField(max_length=255)
    notes = models.TextField()

    def __str__(self):
        return self.name

class Material(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='materials',
    )
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    material_purchase_link = models.URLField(max_length=400)
    notes = models.TextField()

    def __str__(self):
        return self.name
