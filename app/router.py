from rest_framework import routers

from .api import (
    KittiesCRUDViewSet
)

base_router = routers.DefaultRouter()
base_router.register(r'kitties', viewset=KittiesCRUDViewSet, basename='kitty')
