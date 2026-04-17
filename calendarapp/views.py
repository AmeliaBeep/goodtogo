from django.shortcuts import render
from django.views import View
from .models import Event
from .forms import EventForm
from django.db.models.functions import TruncDate
from django.http import JsonResponse, HttpResponseBadRequest
from django.template.loader import render_to_string

class EventListLookupMixin:
    def get_events():
        return Event.objects.all()
    
    def build_events_by_day(self):
        queryset = Event.objects.annotate(start_date=TruncDate('start_time')).order_by('start_date', 'start_time')

        payload = {}
        for event in queryset:
            day_key = str(event.start_date) if event.start_date else "No date"
            if day_key not in payload:
                payload[day_key] = {
                    "date": day_key,
                    "events": []
                }

            payload[day_key]["events"].append(
                {
                    "id": event.id,
                    "title": event.title,
                    "description": event.description,
                    "start_time": event.start_time,
                    "end_time": event.end_time,
                    "weather_required": event.get_weather_required_display(),
                }
            )

        return list(payload.values())

class EventListView(EventListLookupMixin, View):
    def get(self, request):
        events_by_day = self.build_events_by_day()
        events_by_day_html = render_to_string(
            "calendarapp/includes/event_list.html",
            {"events_by_day": events_by_day}  # Pass events to the fragment
        )

        # Return HTML and success status
        return JsonResponse({
            "success": True,
            "html": events_by_day_html
        })

class EventCalendarView(EventListLookupMixin, View):
    pass

class InitialView(EventListLookupMixin, View):

    def get(self, request):
        return render(
        request, 
        "calendarapp/index.html",
    )
