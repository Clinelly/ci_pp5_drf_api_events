from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer
from events_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class EventList(generics.ListCreateAPIView):
    """
    Lists all events.
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Event.objects.all()


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all()
