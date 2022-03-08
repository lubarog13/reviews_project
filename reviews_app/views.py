from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import *
from .serializers import *
import requests
from datetime import datetime


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


class SendReviewView(APIView):
    permission_classes = (IsAdminUser, )

    def get(self, request, id):
        review = Review.objects.get(pk = id)
        post_data = dict(author=review.author.pk, rating=review.rating, review=review.text)
        response = requests.post('https://webhook.site/fcc0ce3f-d15d-4264-a964-8bf28d8fa322', data=post_data)
        if response.status_code == 200:
            review.published = True
            review.save()
            return redirect(request.META.get('HTTP_REFERER'))
        return HttpResponse(status=response.status_code)


class ReviewApiView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_context = {'author': request.user.id}
        serializer = ReviewSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)