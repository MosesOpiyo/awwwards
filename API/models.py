from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.aggregates import Max
from django.core.validators import MinValueValidator,MaxValueValidator
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

    def __str__(self):
        return self.title

    def update(self,new):
        self.title = new.title
        self.date_created = new.date_created
        self.description = new.description
        self.project_link = new.project_link
        self.image = new.image
        self.save()

class Votes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    projects = ForeignKey(Projects,on_delete=CASCADE,null=True)
    design = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    usability = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    content = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    comment = models.TextField()

    def __str__(self):
        return self.user.username + " comment | " + str(self.project.name)