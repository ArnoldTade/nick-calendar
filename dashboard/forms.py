from .models import *
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = {
            # "booking_id",
            "client_name",
            "contact_information",
            "event_date",
            "start_time",
            "end_time",
            "event_type",
            "design_service",
            "number_of_guests",
            "total_cost",
            "downpayment",
            "remaining_payment",
            "payment_status",
            "event_status",
        }
        widgets = {
            "client_name": forms.TextInput(attrs={"class": "form-control "}),
            "contact_information": forms.NumberInput(attrs={"class": "form-control"}),
            "event_date": forms.DateInput(
                attrs={"class": "form-control ", "type": "date"}
            ),
            "start_time": forms.TimeInput(
                attrs={"class": "form-control ", "type": "time"}
            ),
            "end_time": forms.TimeInput(
                attrs={"class": "form-control ", "type": "time"}
            ),
            "event_type": forms.TextInput(attrs={"class": "form-control "}),
            "design_service": forms.TextInput(attrs={"class": "form-control "}),
            "number_of_guests": forms.NumberInput(attrs={"class": "form-control "}),
            "total_cost": forms.NumberInput(attrs={"class": "form-control "}),
            "downpayment": forms.NumberInput(attrs={"class": "form-control "}),
            "remaining_payment": forms.NumberInput(attrs={"class": "form-control "}),
            "payment_status": forms.TextInput(attrs={"class": "form-control "}),
            "event_status": forms.TextInput(attrs={"class": "form-control "}),
        }
