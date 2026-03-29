from django.shortcuts import render
from .models import Event
from .forms import EventForm

def view_home(request):
    events = Event.objects.all()
    return render(
        request, 
        'calendarapp/home.html', 
        {'events': events}
    )

