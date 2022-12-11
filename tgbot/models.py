from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from django.utils.deconstruct import deconstructible

import os
from uuid import uuid4
from stdimage import StdImageField


class User(models.Model):
	LANGUAGE_CHOICES = [
		("ru", "RU"),
		("uz", "UZ")
	]
	REGION_CHOICES = [
		("tashkent", "Tashkent"),
		("samarkand", "Samarkand"),
		("bukhara", "Bukhara"),
		("andijan", "Andijan"),
		("jizzakh", "Jizzakh"),
		("qashqadaryo", "Qashqadaryo"),
		("navoiy", "Qashqadaryo"),
		("namangan", "Namangan"),
		("surxondaryo", "Surxondaryo"),
		("sirdaryo", "Sirdaryo"),
		("fergana", "Fergana"),
		("xorazm", "Xorazm"),
		("karakalpakstan", "Karakalpakstan")
	]
	chat_id = models.CharField(unique=True, max_length=12)
	first_name = models.CharField(null=True, max_length=64)
	username = models.CharField(null=True, blank=True, max_length=32)
	phone_number = models.CharField(null=True, blank=True, max_length=20)
	language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
	region = models.CharField(max_length=32, choices=REGION_CHOICES)
	is_admin = models.BooleanField(default=False)
	is_blocked = models.BooleanField(default=False)
	time_create = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.chat_id} [ {self.first_name} ]"


class Category(MPTTModel):
	name = models.CharField(max_length=32)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return self.name


@deconstructible
class PathAndRename(object):
	def __init__(self, sub_path):
		self.path = sub_path

	def __class__(self, instance, filename):
		ext = filename.split('.')[-1]
		filename = f'{uuid4().hex}.{ext}'

		return os.path.join(self.path, filename)


path_and_rename = PathAndRename("images/post")


class Post(models.Model):
	CURRENCY_CHOICES = [
		("USD", "USD"),
		("UZS", "UZS")
	]
	STATUS_CHOICES = [
		("moderation", "Moderation"),
		("published", "Published"),
		("disabled", "Disabled"),
	]
	
	title = models.CharField(max_length=32)
	description = models.TextField(max_length=360)
	price = models.PositiveIntegerField()
	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
	image = StdImageField(upload_to=path_and_rename, variations={"thumbnail": (420, 420,True)}, blank=True)
	author = models.ForeignKey('User', on_delete=models.CASCADE)
	category = TreeForeignKey('Category', on_delete=models.CASCADE)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

