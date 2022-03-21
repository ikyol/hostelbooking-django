from django.db import models
from django.utils import timezone
from user.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Category(models.Model):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Hostel(models.Model):
    ROOMS_CHOICES = (
        ('1 Room', '1 ROOM'),
        ('2 Rooms', '2 ROOMS'),
        ('3 Rooms', '3 ROOMS'),
        ('4 Rooms', '4 ROOMS'),
    )
    GUESTS_CHOICES = (
        ('1 Guest', '1 GUEST'),
        ('2 Guests', '2 GUESTS'),
        ('3 Guests', '3 GUESTS'),
        ('4 Guests', '4 GUESTS'),
        ('5 Guests', '5 GUESTS'),
        ('6 Guests', '6 GUESTS'),
        ('7 Guests', '7 GUESTS'),
        ('8 Guests', '8 GUESTS'),
    )
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='hostel')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hostel')
    title = models.CharField(max_length=44)
    rooms = models.CharField(max_length=8, choices=ROOMS_CHOICES)
    guests = models.CharField(max_length=8, choices=GUESTS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    services = models.TextField(default='WiFi')
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book')
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='book')
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    is_book = models.BooleanField(default=False)

    def __str__(self):
        return f'From = {self.check_in.strftime("%d-%b-%Y %H:%M")} To = {self.check_out.strftime("%d-%b-%Y %H:%M")}'


class Ratings(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='ratings')
    ratings = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.hostel} -> {self.ratings}'
