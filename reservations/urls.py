from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.make_reservation, name='reservation_form'),
    path('bookings/', views.booking_list, name='booking-list'),
]
