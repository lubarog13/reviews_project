from django.urls import path, include, re_path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', ReviewsListView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', CreateUserView.as_view()),
    path('review/create/', ReviewCreateView.as_view())
]