from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=5, null=True)
    dob = models.DateField(null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
