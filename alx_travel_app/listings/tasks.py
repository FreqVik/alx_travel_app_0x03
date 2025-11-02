from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(user_email, booking_details):
    subject = "Booking Confirmation - ALX Travel"
    message = f"Hello,\n\nYour booking was successful!\n\nDetails:\n{booking_details}\n\nThank you for using ALX Travel."
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, [user_email])
    return f"Email sent to {user_email}"
