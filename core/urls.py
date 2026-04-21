"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.http import HttpResponse
# from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
#
# from housing.views import (ApartmentListCreateAPI, ApartmentRetrieveUpdateDestroyAPI,
#                            BookingAPICreate, BookingAPIRetrieveDestroy,
#                            BookingAPIList, BookingAPIViewApartmentOwnerList, RetrieveUpdateBookingStatusAPIView,
#                            ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView,)
# from users.views import UserAPICreate, MeAPIView, LoginAPI, LogoutAPI, Verify2FAAPIView
#


urlpatterns = [
    path('admin/', admin.site.urls),

    # # JWT
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # AUTH
    path('auth/register/', UserAPICreate.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/verify/', Verify2FAAPIView.as_view(), name='verify-2fa'),
    path('auth/logout/', LogoutAPI.as_view(), name='logout'),
    path('auth/me/', MeAPIView.as_view(), name='me'),

    # APARTMENTS
    path('apartments/', ApartmentListCreateAPI.as_view(), name='apartments-list'),
    path('apartments/<int:pk>/', ApartmentRetrieveUpdateDestroyAPI.as_view(), name='apartment-detail'),

    # REVIEWS
    path('apartments/<int:apartment_pk>/reviews/', ReviewListCreateAPIView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),

    # BOOKINGS
    path('bookings/', BookingAPIList.as_view(), name='bookings-list'),
    path('apartments/<int:apartment_pk>/bookings/', BookingAPICreate.as_view(), name='booking-create'),
    path('bookings/<int:pk>/', BookingAPIRetrieveDestroy.as_view(), name='booking-detail'),

    # OWNER
    path('owner/bookings/', BookingAPIViewApartmentOwnerList.as_view(), name='owner-bookings'),
    path('owner/bookings/<int:pk>/', RetrieveUpdateBookingStatusAPIView.as_view(), name='owner-booking-detail'),
]

# {
#   "user_id": 11,
#   "code": "123456"
# }