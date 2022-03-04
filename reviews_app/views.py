from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import *


class ReviewsListView(ListView):
    model = Review
    template_name = "reviews_list.html"


class ReviewCreateView(CreateView):
    model = Review
    fields = [
        "rating",
        "text"
    ]

    success_url = "/"
    template_name = "review_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_created = timezone.now()
        return super().form_valid(form)


class CreateUserView(CreateView):
    model = User
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "password"
    ]
    success_url = "/accounts/login/"
    template_name = "registration/registration_form.html"

    def form_valid(self, form):
        form.instance.date_joined = timezone.now()
        form.instance.password = make_password(form.instance.password)
        return super().form_valid(form)
