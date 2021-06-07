from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.ForeignKey(User,unique=True,on_delete="CASECADE")
    profile_pic = models.ImageField(verbose_name="Profile Picture",upload_to='profile_pics/')
    birth_day = models.DateField()
    Bio = models.TextField()
