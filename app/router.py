from rest_framework import routers

from .api import (
    KittiesCRUDViewSet,
    BreedsAPIViewSet
)

base_router = routers.DefaultRouter()
base_router.register(r'kitties', viewset=KittiesCRUDViewSet, basename='kitty')
base_router.register(r'breeds', viewset=BreedsAPIViewSet, basename='breed')