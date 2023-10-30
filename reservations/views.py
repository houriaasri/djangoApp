from django.shortcuts import render, redirect
from .models import Booking
from datetime import datetime

from django.http import JsonResponse

def make_reservation(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        reservation_date = request.POST.get('reservation_date')
        reservation_slot = request.POST.get('reservation_slot')


        # Validate the retrieved values
        if not all([first_name, reservation_date, reservation_slot]):
            return JsonResponse({"message": "All fields are required."}, status=400)

        new_booking = Booking(first_name=first_name, reservation_date=reservation_date, reservation_slot=reservation_slot)
        new_booking.save()

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Check if it's an AJAX request
            return JsonResponse({"message": "Réservation réussie!"}, status=201)

        return redirect('booking-list')
    else:
        return render(request, 'reservation_form.html')



def booking_list(request):
    bookings = Booking.objects.all()

    current_date = datetime.now().date()

    return render(request, 'booking_list.html', {'bookings': bookings, 'current_date': current_date})
