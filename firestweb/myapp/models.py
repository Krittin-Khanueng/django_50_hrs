from django.db import models


class Allproduct(models.Model):
	name = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	detail = models.TextField(null=True, blank=True)
