from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CITIZEN = models.BooleanField(default = False)

class UserLoginLogout(models.Model):
    USER = models.ForeignKey(User, related_name = 'user_login_logout', on_delete = models.CASCADE)
    DATE = models.DateField()
    LOGIN = models.TimeField()
    LOGOUT = models.TimeField(blank = True, null = True)

    def __str__(self):
        return f"{self.USER} - {self.DATE} => Login time {self.LOGIN}, Logout time {self.LOGOUT}"

class UserLocation(models.Model):
    USER = models.ForeignKey(User, related_name = 'user_location', on_delete = models.CASCADE)
    DATE = models.DateField()
    LATITUDE = models.DecimalField(max_digits=9, decimal_places=6)
    LONGITUDE = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.USER} - Latitude: {self.LATITUDE} - Longitude: {self.LONGITUDE}"
