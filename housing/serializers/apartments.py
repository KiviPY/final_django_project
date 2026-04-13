from rest_framework import serializers

from housing.models import RegisterApartments, ApartmentImage, Booking
from housing.models.amenity import Amenity


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = '__all__'
        read_only_fields = ('apartment',)


class RegisterApartmentsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RegisterApartments
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'views_count', 'average_rating', 'reviews_count',)
        amenities = serializers.PrimaryKeyRelatedField(queryset=Amenity.objects.all(), many=True)