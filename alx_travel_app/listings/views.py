from rest_framework import viewsets

from alx_travel_app.listings.tasks import send_booking_confirmation_email
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        user_email = booking.user.email
        booking_details = (
            f"Listing: {booking.listing.title}\n"
            f"Check-in: {booking.check_in_date}\n"
            f"Check-out: {booking.check_out_date}\n"
            f"Guests: {booking.guests}"
        )

        # ✅ Trigger Celery background task
        send_booking_confirmation_email.delay(user_email, booking_details)