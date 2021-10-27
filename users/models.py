from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    profile_pic = CloudinaryField(blank=True,null=True)