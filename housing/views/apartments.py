from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from housing.filters import ApartmentFilter
from housing.models import RegisterApartments
from housing.permissions import IsOwnerOrReadOnly
from housing.serializers import RegisterApartmentsSerializer


class ApartmentListCreateAPI(generics.ListCreateAPIView):
    queryset = RegisterApartments.objects.all()
    serializer_class = RegisterApartmentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # любой может смотреть, только авторизованные могут создать
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter


class ApartmentRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegisterApartments.objects.all()
    serializer_class = RegisterApartmentsSerializer
    permission_classes = [IsOwnerOrReadOnly]  # только владелец может изменять или удалять


