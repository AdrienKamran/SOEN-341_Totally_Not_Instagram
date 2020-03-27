from django.db import models
from django.contrib.auth.models import User
import datetime

class userProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

class Image(models.Model):
    name = models.CharField(max_length=50, unique=True)
    caption = models.CharField(max_length=50, unique=False)
    Img = models.ImageField(upload_to='images/', unique=False)
    user = models.ForeignKey (User,on_delete=models.CASCADE)
    post_date = models.DateField(("Date"), default=datetime.date.today, unique=False)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-post_date',]

class Comment(models.Model):
    user = models.ForeignKey (User,on_delete=models.CASCADE)
    img = models.ForeignKey (Image,on_delete=models.CASCADE)
    msg = models.CharField(max_length=1024)
    post_date = models.DateField(("Date"), default=datetime.date.today)