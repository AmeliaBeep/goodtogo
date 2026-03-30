from django.urls import path
from . import views

urlpatterns = [
    path("", views.InitialEventListView.as_view(), name="home"),
    path("api/get-list-view", views.EventListView.as_view(), name="list_view"),
    path("api/get-calendar-view", views.EventCalendarView.as_view(), name="calendar_view")
]
