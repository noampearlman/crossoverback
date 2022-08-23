from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
 
# test data
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
 
 
class Kid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    age = models.IntegerField()

# real data
class Property(models.Model):
    name = models.TextField()
    page_Content = models.TextField(default="NO INFORMATION YET")
    date_created = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    is_verified = models.IntegerField(default=0)

class Direction(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField(default ="NO DESC")

class Type(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField(default ="NO DESC")

class Connection(models.Model):
    firstProperty = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, related_name='firstProperty')
    secondProperty = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, related_name='secondProperty')
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    desc = models.TextField(default ="NO DESC")
    date_created = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    is_verified = models.IntegerField(default =0)
