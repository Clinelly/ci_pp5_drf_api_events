from rest_framework import generics, permissions
from .models import Attending
from .serializers import AttendingSerializer
from events_api.permissions import IsOwnerOrReadOnly
# Create your views here.


class AttendingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AttendingSerializer
    queryset = Attending.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendingSerializer
    queryset = Attending.objects.all()
