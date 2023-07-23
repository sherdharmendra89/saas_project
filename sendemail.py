from django.core.mail import send_mail
from django.conf import settings


def send_registraion_email(email):
        subject="Registration Successfull MSG",
        message="Thank you for registering with us. Your registration was successful.",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=["sherdharmendra89@gmail.com"],
        send_mail(subject, message, from_email, recipient_list)
        # return email




