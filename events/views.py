from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from events_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class EventList(APIView):
    """
    Lists all events.
    No create (POST) method.
    Profile creation handled by Django signals.
    """
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(
            events, many=True, context={'request': request}
        )
        return Response(serializer.data)
