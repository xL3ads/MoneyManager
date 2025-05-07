
from django.urls import path
from dashboard import views
urlpatterns=[
    path('dashboard/', views.dashboard_view, name='dashboard'),
]