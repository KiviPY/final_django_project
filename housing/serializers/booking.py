from rest_framework import serializers
from housing.models import Booking
from django.core.mail import send_mail

def send_booking_email(booking):
    """booking - это просто экземпляр записи в базе данных, где хранится: какая квартира забронирована, кем и в каком статусе.
    Например: booking.apartment.title --> "Cozy Studio in Leipzig", booking.user.username --> # "kyrylo"
"""
    owner = booking.apartment.user  # это владелец квартиры
    to_email = owner.email
    subject = f"{booking.user.username} is interested in your apartment {booking.apartment.title}" # Theme of mail
    message = f"""Hello {owner.username},
               
    f"{booking.user.username} wants to book your apartment {booking.apartment.title}.

    Now status is {booking.apartment.status}. If you want to chat with {booking.user.username}, change it please
    """
    send_mail(subject, message, 'noreply@yourapp.com', [to_email], fail_silently=False)


class BookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = 'status'




class BookingApartmentsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('apartment', 'status')
