from django.forms import ModelForm
from django import forms
from main.models import Hostel, Comment, Book
from captcha.fields import CaptchaField
import datetime


class CreateHostelForm(ModelForm):
    class Meta:
        model = Hostel
        fields = ['category', 'title', 'rooms', 'guests', 'price', 'description', 'services', 'rating', 'created_at',
                  'image']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateHostelForm, self).__init__(*args, **kwargs)

    def save(self):
        data = self.cleaned_data
        data['author'] = self.request.user
        hostel = Hostel.objects.create(**data)
        return hostel


class UpdateHostelForm(ModelForm):
    class Meta:
        model = Hostel
        fields = ['category', 'title', 'rooms', 'guests', 'price', 'description', 'services', 'rating', 'created_at',
                  'image']


class CommentForm(ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Comment here ...',
        'rows': '4',
    }))
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['comment']


class BookingForm(ModelForm):
    check_in = forms.DateTimeField(widget=forms.DateTimeInput())
    check_out = forms.DateTimeField(widget=forms.DateTimeInput())

    class Meta:
        model = Book
        fields = ['hostel', 'check_in', 'check_out']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(BookingForm, self).__init__(*args, **kwargs)

    def clean(self):
        check_in = self.cleaned_data.get('check_in')
        check_out = self.cleaned_data.get('check_out')
        if Book.objects.filter(check_in=check_out).exists():
            raise forms.ValidationError('Бронируйте как минимум на один день')
        return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        data['user'] = self.request.user
        is_book = Book.objects.create(**data)
        return is_book
