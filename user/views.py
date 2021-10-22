from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import send_success_email


# def register(request):
#     form = CreateUserForm()
#
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('first_name')
#             messages.success(request, 'Your user successfully created' + user)
#             return redirect('login')
#     context = {'form': form}
#     return render(request, 'register.html', context)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class SignUpView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        send_success_email.delay(form.instance.email)
        return super().form_valid(form)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Email or Password incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('homepage')
