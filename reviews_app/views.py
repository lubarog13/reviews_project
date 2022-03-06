from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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



class ReviewsListAPIView(ListAPIView):
        serializer_class = ReviewSerializer
        queryset = Review.objects.all()


class ReviewCreateApiView(APIView):
    def post(self, request):
        if request.user.is_anonymous == False:
            request.data._mutable = True
            request.data['author'] = request.user.id
            request.data['date_created'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            request.data._mutable = False
            serializer = ReviewSimpleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)     
        return Response(status=status.HTTP_401_UNAUTHORIZED)          