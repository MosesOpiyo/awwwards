from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import CharField, DateField, EmailField, IntegerField,TextField
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    title = CharField(max_length=100)
    image = CloudinaryField()
    description = TextField()
    project_link = TextField()
    date_added = DateField()

class Votes(models.Model):
    design = IntegerField()
    usability = IntegerField()
    content = IntegerField()