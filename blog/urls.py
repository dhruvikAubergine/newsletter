from django.contrib import admin
from django.urls import path, include
from .views import SubscribeView, BlogView, BlogDetailView

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-details'),
]