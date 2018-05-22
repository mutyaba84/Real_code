from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.

class profiles(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name



# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length = 40)
    title = models.CharField(max_length = 50)
    bio = models.TextField(max_length = 1000)
    def __str__(self):
       return self.name

class Track(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 1000)
    def __str__(self):
       return self.title

class Session(models.Model):
    title = models.CharField(max_length = 50);
    abstract = models.TextField(max_length = 2000);
    track = models.ForeignKey(Track);
	#speaker = models.CharField(Speaker)
    def __str__(self):
       return self.title