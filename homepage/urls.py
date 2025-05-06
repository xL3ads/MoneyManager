from django.urls import path

import homepage
from homepage import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
]