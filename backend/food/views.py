# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from food.models import Food
from food.serializers import FoodSerializer
from rest_framework import generics
from django.shortcuts import render

# Create your views here.
class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer