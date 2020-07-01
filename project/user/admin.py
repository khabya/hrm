from django.contrib import admin
from .models import (
    User, 
    UserLoginLogout, 
    UserLocation,
)

admin.site.register(User)
admin.site.register(UserLoginLogout)
admin.site.register(UserLocation)
