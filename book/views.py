import datetime
from socket import SO_BROADCAST
from django.views.generic import ListView

from main.models import Hostel



class MainPageView(ListView):
    model = Hostel
    template_name = 'index.html'
    context_object_name = 'hostels'

