from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from housing.filters import ApartmentFilter
from housing.models import RegisterApartments
from housing.permissions import IsOwnerOrReadOnly, IsApartmentOwner
from housing.serializers import RegisterApartmentsSerializer


class ApartmentListCreateAPI(generics.ListCreateAPIView):
    queryset = RegisterApartments.objects.all()
    serializer_class = RegisterApartmentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # любой может смотреть, только авторизованные могут создать
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ApartmentFilter
    ordering_fields = ['average_rating', 'created_at', 'views_count', 'price_per_month']

class ApartmentRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegisterApartments.objects.all()
    serializer_class = RegisterApartmentsSerializer
    permission_classes = [IsOwnerOrReadOnly]  # только владелец может изменять или удалять




class MyApartmentListAPI(generics.ListAPIView):
    serializer_class = RegisterApartmentsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ApartmentFilter
    ordering_fields = ['average_rating', 'created_at', 'views_count', 'price_per_month']

    def get_queryset(self):
        return RegisterApartments.objects.filter(user=self.request.user)


class MyApartmentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegisterApartments.objects.all()
    serializer_class = RegisterApartmentsSerializer
    permission_classes = [IsApartmentOwner]

