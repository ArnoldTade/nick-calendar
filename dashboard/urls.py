from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.BASE), name="BASE"),
    path("Tables/", views.tables, name="tables"),
    path("Forms/", views.forms, name="forms"),
    path("Charts/", views.charts, name="charts"),
    path("calendar/", views.calendar, name="calendar"),
    path("view-calendar/<int:id>/", views.viewCalendar, name="view-calendar"),
]
