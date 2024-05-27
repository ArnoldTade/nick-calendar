from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from datetime import datetime, time
from .forms import *


def BASE(request):
    return render(request, "base.html")


def tables(request):
    return render(request, "Tables.html")


def forms(request):
    return render(request, "Forms.html")


def charts(request):
    return render(request, "Charts.html")


def viewCalendar(request, id=None):
    books = {}
    book = get_object_or_404(Booking, id=id)
    bookform = BookingForm(request.POST, instance=book)
    if bookform.is_valid():
        bookform.save()
        return redirect("view-calendar", id=book)
    bookform = BookingForm(instance=book)
    books["bookform"] = bookform
    all_events = Booking.objects.all()
    #### CALENDAR #####
    bookings = []
    customer_book = Booking.objects.filter(id=id)
    for book in customer_book:
        start_date = datetime.combine(book.event_date, book.start_time)
        end_datetime = datetime.combine(book.event_date, book.end_time)

        booking = {
            "title": f"{book.event_type}",
            "start": start_date.isoformat(),
            "end": end_datetime.isoformat(),
        }
        bookings.append(booking)

    return render(
        request,
        "Calendar.html",
        {
            "bookform": bookform,
            "bookings": bookings,
            "all_events": all_events,
        },
    )


def calendar(request):
    all_events = Booking.objects.all()

    return render(
        request,
        "Calendar.html",
        {
            "all_events": all_events,
        },
    )
