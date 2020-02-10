from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username

class Image(models.Model):
    name = models.CharField(max_length=50)
    Img = models.ImageField(upload_to='images/')
