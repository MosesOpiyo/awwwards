from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, EmailField, IntegerField,TextField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    user = ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    image = CloudinaryField()
    description = models.TextField()
    project_link = models.TextField()
    date_added = models.DateField()

class Votes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    projects = ForeignKey(Projects,on_delete=CASCADE,null=True)
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()