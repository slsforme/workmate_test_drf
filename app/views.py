from django.shortcuts import render
from rest_framework import generics
from .models import (
    Kitty,
    Breed
)

class KittyAPIView(generics.ListAPIView):
    queryset = Kitty.objects.all()



