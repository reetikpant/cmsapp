from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Users(models.Model):

    user_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default=1)
    password = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user_id

class Posts(models.Model):
    post_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    creation_date = models.CharField(max_length=200)
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    access=models.CharField(max_length=200, default=1)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.post_id



class Likes(models.Model):
    like_id = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Likes"

    def __str__(self):
        return self.like_id

