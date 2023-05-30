from django.test import TestCase, Client
from django.urls import reverse
from .models import User


class GetUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            uid=1,
            username='testuser',
            nickname='Test User',
            avatar='test.jpg',
            signature='Hello, world!',
            fans=10,
            follow=20,
            exp=100,
        )

    def test_get_user(self):
        response = self.client.get(reverse('get_user', args=[self.user.uid]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'uid': self.user.uid,
            'username': self.user.username,
            'nickname': self.user.nickname,
            'avatar': self.user.avatar,
            'signature': self.user.signature,
            'fans': self.user.fans,
            'follow': self.user.follow,
            'exp': self.user.exp,
            'level': self.user.getLevel(),
        })

    def test_get_nonexistent_user(self):
        response = self.client.get(reverse('get_user', args=[999]))
        self.assertEqual(response.status_code, 404)