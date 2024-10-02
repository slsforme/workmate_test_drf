from rest_framework import serializers
from .models import (
    Kitty,
    Breed,
)


class KittySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitty
        fields = '__all__'


class BreedSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'