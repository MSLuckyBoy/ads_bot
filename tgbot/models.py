from django.db import models


class User(models.Model):
	chat_id = models.PositiveBigIntegerField(unique=True)
	first_name = models.CharField(null=True, max_length=64)
	username = models.CharField(null=True, blank=True, max_length=32)
	phone_number = models.CharField(null=True, blank=True, max_length=20)
	language = models.CharField(max_length=10)
	region = models.CharField(null=True, blank=True, max_length=32)
	time_create = models.DateTimeField(auto_now_add=True)
