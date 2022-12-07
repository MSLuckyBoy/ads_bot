from django.db import models


class User(models.Model):
	chat_id = models.CharField(unique=True, max_length=12)
	first_name = models.CharField(null=True, max_length=64)
	username = models.CharField(null=True, blank=True, max_length=32)
	phone_number = models.CharField(null=True, blank=True, max_length=20)
	language = models.CharField(max_length=10)
	region = models.CharField(null=True, blank=True, max_length=32)
	time_create = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
		return self.name


class Subcategory(models.Model):
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	name = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.category} / {self.name}"


class Brand(models.Model):
	subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
	name = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.subcategory} / {self.name}"


class Ad(models.Model):
	CURRENCY_CHOICES = [
		("USD", "(USD) Dollar"),
		("UZS", "(UZS) Sum")
	]
	
	title = models.CharField(max_length=32)
	brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
	description = models.TextField(max_length=360)
	price = models.PositiveIntegerField()
	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
	telegram_image_id = models.CharField(null=True, blank=True, max_length=100)

	def __str__(self):
		return self.title

