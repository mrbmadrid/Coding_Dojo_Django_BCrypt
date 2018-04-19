# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(unique=True, max_length=60)
	salt = models.CharField(max_length=255)
	pw = models.CharField(max_length=255)

	def __repr__(self):
		return "<{} {} {}>".format(self.last_name, self.first_name, self.email)
