from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,null=True)
    profile_pic = CloudinaryField(null=True,blank=True)
    user_bio = models.TextField() 
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100) 