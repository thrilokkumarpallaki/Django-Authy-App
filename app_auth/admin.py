from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileModel(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileModel)
