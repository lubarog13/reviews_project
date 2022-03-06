from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('', ReviewsListView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', CreateUserView.as_view()),
    path('review/create/', ReviewCreateView.as_view()),
    path('review/send/', csrf_exempt(SendReviewView.as_view())),
    path('api/reviews/', ReviewsListAPIView.as_view()),
    path('api/review/create/', ReviewCreateApiView.as_view())
]