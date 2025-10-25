from datetime import date
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Show, BandMember


def home(request):
    upcoming = Show.objects.filter(date__gte=date.today()).order_by('date')[:3]
    return render(request, 'band/home.html', {"upcoming": upcoming})


def about(request):
    members = BandMember.objects.order_by('name')
    return render(request, 'band/about.html', {'members': members})


class ShowList(ListView):
    model = Show
    template_name = 'band/shows.html'
    context_object_name = 'shows'
    ordering = ['date']

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
