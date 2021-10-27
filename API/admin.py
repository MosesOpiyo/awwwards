from django.contrib import admin
from users.models import User
from API.models import Projects,Votes


# Register your models here.
admin.site.register(User)
admin.site.register(Projects)
admin.site.register(Votes)