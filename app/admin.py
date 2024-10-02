from django.contrib import admin

from .models import (
    Kitty,
    Breed
)

admin.site.register(Kitty)
admin.site.register(Breed)