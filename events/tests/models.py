from django.test import TestCase
from django.contrib.auth.models import User
from events.models import Event


class EventModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_event_creation(self):
        event = Event.objects.create(
            owner=self.user,
            title='Test Event',
            start_time='2023-01-01 12:00',
            end_time='2023-01-02 12:00'
        )
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.owner, self.user)
        self.assertIsNotNone(event.created_at)
        self.assertIsNotNone(event.updated_at)

    def test_event_string_representation(self):
        event = Event.objects.create(
            owner=self.user,
            title='Test Event',
            start_time='2023-01-01 12:00',
            end_time='2023-01-02 12:00'
        )
        expected_string = f"{event.id} {event.title}"
        self.assertEqual(str(event), expected_string)

    def test_event_ordering(self):
        event1 = Event.objects.create(
            owner=self.user,
            title='Event 1',
            start_time='2023-01-01 12:00',
            end_time='2023-01-02 12:00'
        )
        event2 = Event.objects.create(
            owner=self.user,
            title='Event 2',
            start_time='2023-02-01 12:00',
            end_time='2023-02-02 12:00'
        )
        event3 = Event.objects.create(
            owner=self.user,
            title='Event 3',
            start_time='2023-03-01 12:00',
            end_time='2023-03-02 12:00'
        )
        events = Event.objects.all()
        self.assertEqual(events[0], event3)
        self.assertEqual(events[1], event2)
        self.assertEqual(events[2], event1)
