from django.contrib import admin
from jrc_profile.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
