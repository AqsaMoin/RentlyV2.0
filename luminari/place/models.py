from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.

class Place(models.Model):
    place_img = models.FileField(upload_to='images/')
    place_title = models.CharField(max_length=200)
    place_desc = models.TextField()
    place_category = models.CharField(max_length=50,blank=True)
    slug = AutoSlugField(populate_from='place_title',always_update=True)

    def __str__(self):
        return self.place_title