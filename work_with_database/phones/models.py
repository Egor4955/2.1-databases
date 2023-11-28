from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField()
    image = models.FilePathField()
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField()




