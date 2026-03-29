from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.db.models.functions import TruncDate

class EventListLookupMixin:
    def get_events():
        return Event.objects.all()
    
    def build_events_by_day():
        queryset = Event.objects.annotate(start_date=TruncDate('start_time')).order_by('start_date', 'start_time')

        payload = {}
        for event in queryset:
            day_key = str(event.start_date) if event.start_date else "No date"
            if day_key not in payload:
                payload[day_key] = {
                    "day": day_key,
                    "items": []
                }

            payload[day_key]["items"].append(
                {
                    "id": event.id,
                    "title": event.title,
                    "description": event.description,
                    "start_time": event.start_time,
                    "end_time": event.end_time,
                    "weather_required": event.weather_required,
                }
            )

        return list(payload.values())


def view_home(request):
    events = Event.objects.all()
    events_by_day = EventListLookupMixin.build_events_by_day()
    return render(
        request, 
        'calendarapp/home.html', 
        {
            'events': events,
            'events_by_day': events_by_day
        }
    )

