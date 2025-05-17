from django.urls import path

from categories import views

urlpatterns = [
    path('add_category/', views.CategoryCreateView.as_view(), name='add-category'),
    path('list_category/', views.CategoryListView.as_view(), name='list-category'),
    path('delete_category/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete-category'),
]