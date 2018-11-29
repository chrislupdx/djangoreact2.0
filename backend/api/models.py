# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Todo(models.Model):
	name = models.CharField(max_length=25)
	date = models.DateTimeField(blank=True, null=True)
	finished = models.BooleanField()

	class Meta:
		abstract = True
		app_label = 'app_label'

def __str__(self):
	"""A string representation of the model."""
	return self.title
