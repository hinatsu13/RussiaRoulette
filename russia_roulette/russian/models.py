from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, null=True, max_length=10)

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    phone_number = models.CharField(blank=True, null=True, unique=True, max_length=10)
    event = models.ManyToManyField("russian.Event")

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    point_reward = models.IntegerField(default=0)
    admin = models.ForeignKey("russian.Admin", on_delete=models.CASCADE)
    reward = models.ManyToManyField("russian.Reward")

class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
