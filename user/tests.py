from django.test import TestCase, Client
from django.urls import reverse
from user.models import *
import json


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.login_url = reverse('login')
        self.user1 = User.objects.create(
            email='krakem.nc@gmail.com',
            password='12345678',
        )

    def testLoginGet(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def testLoginPOST(self):
        user1 = User.objects.create(
            email='krakem.nc@gmail.com',
            password='12345678',
        )
        response = self.client.post(self.login_url, {
            'email': 'krakem.nc@gmail.com',
            'password': '12345678'
        })

        self.assertEqual(response.status_code, 302)


class TestModels(TestCase):

    def test_models(self):
        user = User.objects.create(
            email='krakem.nc@gmail.com',
            password='qwerty123'
        )
        user.save()
        self.assertEqual(str(user), 'krakem.nc@gmail.com')
