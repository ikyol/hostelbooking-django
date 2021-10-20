from django.urls import path
from main.views import *

urlpatterns = [
    path('room-detail/<int:id>/', HostelDetailView.as_view(), name='room-detail'),
    path('rooms/', HostelListView.as_view(), name='hostels'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('about-us/', AboutUsView.as_view(), name='about'),
    path('hostel-create/', HostelCreateView.as_view(), name='hostel-create'),
    path('hostel-update/<int:id>/', HostelUpdateView.as_view(), name='hostel-update'),
    path('hostel-delete/<int:id>/', HostelDeleteView.as_view(), name='hostel-delete'),
    path('hostel-search/', HostelSearchView.as_view(), name='hostel-search'),
    path('booking/', BookingView.as_view(), name='booking'),
]
