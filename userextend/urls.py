from django.urls import path

from userextend import views

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('view_profile/<int:pk>/', views.UserDetailView.as_view(), name='view-profile'),
    path('edit_profile/<int:pk>/', views.UserEditView.as_view(), name='edit-profile')
]