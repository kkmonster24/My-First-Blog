from django.db import models
from django.urls import reverse 

# Create your models here.

class Post(models.Model):
	title		=	models.CharField(max_length=250)
	image		=	models.TextField(null=True,blank=True)
	content		=	models.TextField()
	updated		= 	models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp	=	models.DateTimeField(auto_now=False,auto_now_add=True)

	
		