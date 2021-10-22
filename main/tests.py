from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from .models import Hostel, Category
from django.contrib.auth import get_user_model
import json

User = get_user_model()


class HostelTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='krakem.nc@gmail.com', password='qwerty')
        self.category = Category.objects.create(title='Hostels', slug='hostels')
        self.hostel = Hostel.objects.create(
            category=self.category,
            title='Test',
            price=Decimal('150.00')
        )
