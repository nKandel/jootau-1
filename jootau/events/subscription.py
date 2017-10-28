from .models import Subscription, Location, EventType
from django.http import HttpResponse


def load_subscription(request):
    '''loads subscription in the database'''

    location = Location.objects.all()
    event_type = EventType.objects.all()
    
    for loc in location:
        for event in event_type:
            subscription = Subscription()
            subscription.location = loc
            subscription.event_type = event
            subscription.save()
    return HttpResponse("Subscription saved")

    
