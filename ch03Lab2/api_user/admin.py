from django.contrib import admin

# Register your models here.
from api_user.models import User

admin.site.register(User)