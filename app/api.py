from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import ( 
    viewsets, 
    mixins,
    generics
)

from .models import (
    Kitty,
    Breed,
)

from .serializers import (
    KittySerializer,
    BreedSerilizer
)

class KittiesCRUDViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Kitty.objects.all()
    serializer_class = KittySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed', 'breed__name']


class BreedsAPIViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerilizer

