from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'