# from django.contrib.auth.models import User
# from .models import Comment, Event
# from rest_framework import status
# from rest_framework.test import APITestCase


# class CommentListViewTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='user1',
#             password='pass1'
#             )

#     def test_can_list_comments(self):
#         user = User.objects.get(username='user1')
#         Comment.objects.create(
#             owner=user,
#             content="Content"
#         )
#         response = self.client.get('/comments/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_logged_in_user_can_create_comments(self):
#         self.client.login(username="user1", password="pass1")
#         response = self.client.post('/comments/',
#                                     {'content': 'Content',
#                                      'owner': self.user.id})
#         count = Comment.objects.count()
#         self.assertEqual(count, 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_user_not_logged_in_cant_create_event(self):
#         response = self.client.post('/comments/',
#                                     {'content': 'Content',
#                                      'owner': self.user.id})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class CommentDetailViewTests(APITestCase):
#     def setUp(self):
#         user1 = User.objects.create_user(username='user1', password='pass1')
#         user2 = User.objects.create_user(username='user2', password='pass2')
#         comment1 = Comment.objects.create(
#             owner=user1,
#             content="Content 1"
#         )
#         comemnt2 = Comment.objects.create(
#             owner=user2,
#             content="Content 2"
#         )

#     def test_can_retrieve_comment_using_valid_id(self):
#         response = self.client.get('/comments/1/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['content'], 'Comment 1 content')

#     def test_cant_retrieve_comment_using_invalid_id(self):
#         response = self.client.get('/comments/999/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_user_can_update_own_comment(self):
#         self.client.login(username='user1', password='pass1')
#         response = self.client.put('/comments/1/',
#                                    {'content': 'Content',
#                                     'owner': self.user.id})
#         comment = Comment.objects.get(pk=1)
#         self.assertEqual(comment.content, 'New Content')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_cant_update_another_users_comment(self):
#         self.client.login(username='user1', password='pass1')
#         response = self.client.put('/comments/2/',
#                                    {'content': 'Content',
#                                     'owner': self.user.id})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_user_can_delete_own_comment(self):
#         self.client.login(username='user1', password='pass1')
#         response = self.client.delete('/comments/1/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_user_cant_delete_another_users_comment(self):
#         self.client.login(username='user1', password='pass1')
#         response = self.client.delete('/comments/2/')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
