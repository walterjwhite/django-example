from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .contact_form import ContactForm
import os


def send_email_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_email(form)
                messages.success(request, "Email sent successfully!")
            except BadHeaderError:
                messages.error(request, "Invalid header found. Email not sent.")

            except Exception as e:
                messages.error(request, f"Failed to send email: {str(e)}")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


def send_email(form):
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")

    recipient = form.cleaned_data["sender"]
    subject = recipient + " wrote " + form.cleaned_data["subject"]
    message = form.cleaned_data["message"]

    send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
