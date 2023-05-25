from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.


class EventListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass1')

    def test_can_list_events(self):
        user = User.objects.get(username='user1')
        Event.objects.create(
            owner=user,
            title="Event Title",
            start_time="2023-01-01 12:00",
            end_time="2023-01-02 12:00"
            )
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_event(self):
        self.client.login(username="user1", password="pass1")
        response = self.client.post('/events/', {'title': 'Title', 'start_time': '2023-01-01 12:00', 'end_time': '2023-01-02 12:00', 'owner': self.user.id})
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_event(self):
        response = self.client.post('/events/', {'title': 'Title', 'start_time': '2023-01-01 12:00', 'end_time': '2023-01-02 12:00'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EventDetailViewTests(APITestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')
        Event.objects.create(
            owner=user1,
            title='Event 1 title',
            description='Event 1 description',
            start_time="2023-01-01 12:00",
            end_time="2023-01-02 12:00"
        )
        Event.objects.create(
            owner=user2,
            title='Event2 title',
            description='Event 2 description',
            start_time="2023-02-01 12:00",
            end_time="2023-02-02 12:00"
        )

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get('/events/1/')
        self.assertEqual(response.data['title'], 'Event 1 title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get('/events/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put('/events/1/', {'title': 'Event 1 title'})
        event = Event.objects.filter(pk=1).first()
        self.assertEqual(event.title, 'Event 1 new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_event(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put('/events/2/', {'title': 'Event 2 new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
