from django.contrib import admin
from users.models import Profile, User
from API.models import Projects,Votes


# Register your models here.
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Votes)