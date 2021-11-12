from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *


class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        hostel = self.get_object()
        return self.request.user.is_authenticated and self.request.user == hostel.author


class MainPageView(ListView):
    model = Hostel
    template_name = 'index.html'
    context_object_name = 'hostels'


class HostelDetailView(DetailView):
    model = Hostel
    template_name = 'room-details.html'
    context_object_name = 'hostel'
    pk_url_kwarg = 'id'

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            hostel = self.get_object()
            form.instance.author = request.user
            form.instance.hostel = hostel
            form.save()

            return redirect(reverse("room-detail", kwargs={
                'id': hostel.id,
            }))

    def get_context_data(self, **kwargs):
        hostel_comments = Comment.objects.all().filter(hostel=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'hostel_comments': hostel_comments,
        })
        return context


class HostelListView(ListView):
    model = Hostel
    template_name = 'rooms.html'
    context_object_name = 'hostels'
    paginate_by = 1


class ContactView(ListView):
    model = Hostel
    template_name = 'contact.html'
    context_object_name = 'contact'


class AboutUsView(ListView):
    model = Hostel
    template_name = 'about-us.html'
    context_object_name = 'about'


class HostelCreateView(CreateView):
    model = Hostel
    template_name = 'hostel-create.html'
    form_class = CreateHostelForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('room-detail', args=(self.object.id,))


class HostelUpdateView(IsAuthorMixin, UpdateView):
    model = Hostel
    template_name = 'hostel-update.html'
    form_class = UpdateHostelForm
    context_object_name = 'hostel_form'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return reverse('room-detail', kwargs={'id': self.kwargs['id']})


class HostelDeleteView(IsAuthorMixin, DeleteView):
    model = Hostel
    template_name = 'hostel-delete.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('hostels')


class HostelSearchView(ListView):
    model = Hostel
    template_name = 'hostel-search.html'
    context_object_name = 'hostels'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if not q:
            return Hostel.objects.none()
        queryset = queryset.filter(Q(title__icontains=q) | Q(price__icontains=q) | Q(rooms__icontains=q))
        return queryset


class BookingView(CreateView):
    model = Book
    form_class = BookingForm
    template_name = 'booking.html'
    pk_url_kwarg = 'id'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('homepage')
