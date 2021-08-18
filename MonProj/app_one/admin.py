from django.contrib import admin
from .models import User_Authentication, UserProfileInfo

# Register your models here.
admin.site.register(User_Authentication)
admin.site.register(UserProfileInfo)


# Admin details...
"""
username - admin
password - testpassword
email- admin@django.com
"""