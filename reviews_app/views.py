from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views import View
from .models import *
import requests


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


class SendReviewView(View):
    def post(self, request):
        if request.user.is_superuser:
            id = request.POST.get('review_id', '')
            review = Review.objects.get(pk = id)
            post_data = dict(author=review.author.pk, rating=review.rating, review=review.text)
            response = requests.post('https://webhook.site/fcc0ce3f-d15d-4264-a964-8bf28d8fa322', data=post_data)
            if response.status_code == 200:
                review.published = True
                review.save()
            return(HttpResponse(status=response.status_code))
        return (HttpResponse(status=401))