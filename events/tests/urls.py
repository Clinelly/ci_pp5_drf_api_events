from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from events.models import Event


class EventUrlsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1',
                                             password='pass1')
        self.event = Event.objects.create(
            owner=self.user,
            title='Test Event',
            start_time='2023-01-01T12:00:00Z',
            end_time='2023-01-02T12:00:00Z'
        )

    def test_event_list_url(self):
        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_detail_url(self):
        url = reverse('event-detail', args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_detail_url_with_invalid_id(self):
        url = reverse('event-detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
