from django.contrib.auth.models import User
from django.db import models
class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)