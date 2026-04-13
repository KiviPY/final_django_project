from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from housing.filters import BookingFilter
from housing.permissions import IsOwner, IsApartmentOwner

from housing.models import RegisterApartments, Booking
from housing.serializers import BookingApartmentsSerializer
from housing.serializers.booking import BookingStatusSerializer, send_booking_email


# Create your views here.





class BookingAPICreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingApartmentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Берёт apartment_pk из URL (/apartments/1/book/ -> apartment_pk = 1)
           Находит объект RegisterApartments с этим id
           Сохраняет booking, привязывая его к апартаменту
           user берётся автоматически через Hidden поле в сериализаторе"""
        apartment_id = self.kwargs.get('apartment_pk')
        apartment = RegisterApartments.objects.get(id=apartment_id)
        booking = serializer.save(apartment=apartment)

        # отправка email
        send_booking_email(booking)


class BookingAPIRetrieveDestroy(generics. RetrieveDestroyAPIView):
    serializer_class = BookingApartmentsSerializer
    permission_classes = [IsOwner]
    def get_queryset(self):
        """фильтрует все объекты Booking, оставляя только те, которые принадлежат текущему пользователю"""
        return Booking.objects.filter(user=self.request.user)



class BookingAPIList(generics.ListAPIView):
    serializer_class = BookingApartmentsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookingFilter

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)



class BookingAPIViewApartmentOwnerList(generics.ListAPIView):
    serializer_class = BookingStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookingFilter

    def get_queryset(self):
        # возвращаем все бронирования для квартир текущего пользователя
        return Booking.objects.filter(apartment__user=self.request.user)


class RetrieveUpdateBookingStatusAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = BookingStatusSerializer  # сериализатор только для поля status
    permission_classes = [IsApartmentOwner]  # владелец квартиры может менять статус

    def get_queryset(self):
        # возвращаем все бронирования для квартир текущего пользователя
        return Booking.objects.filter(apartment__user=self.request.user)









# class ApartmentViewSet(viewsets.ModelViewSet):
#     queryset = RegisterApartments.objects.all()
#     serializer_class = RegisterApartmentsSerializer
#
#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             return [permissions.AllowAny()]
#         elif self.action == 'create':
#             return [permissions.IsAuthenticated()]
#         else:  # update, partial_update, destroy
#             return [IsOwnerOrReadOnly()]