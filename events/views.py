from rest_framework import generics, permissions, filters
from .models import Event
from .serializers import EventSerializer
from events_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class EventList(generics.ListCreateAPIView):
    """
    Lists all events.
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        attending_count=Count('attending', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'attending__owner__profile',
    ]
    search_fields = [
        "owner__username",
        "title",
    ]
    ordering_fields = [
        'attending_count',
        'likes_count',
        'likes__created_at',
        'comment_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        attending_count=Count('attending', distinct=True)
    ).order_by('-created_at')
