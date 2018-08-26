# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    food_class = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    benefits = models.TextField(max_length=500)
