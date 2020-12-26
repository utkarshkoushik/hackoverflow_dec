from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hackathon(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    unique_code = models.CharField(max_length=255,null=True,blank=True)

class userData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    college = models.CharField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    year = models.CharField(max_length=20,null=True,blank=True)
    current_hackathon = models.ForeignKey(Hackathon,on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    unique_code = models.CharField(max_length=255,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TeamMember(models.Model):
    member = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    group_type = models.CharField(max_length=255,null=True,blank=True)
    unique_code = models.CharField(max_length=255,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class GroupMember(models.Model):
    member = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    message = models.TextField(blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)