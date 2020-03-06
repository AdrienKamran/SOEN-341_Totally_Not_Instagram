from django.contrib import admin
from timeline.models import userProfile, Image, Comment

admin.site.register(userProfile)

admin.site.register(Image)
admin.site.register(Comment)