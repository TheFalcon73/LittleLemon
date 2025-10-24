from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.BookingListCreate.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingRetrieveUpdateDestroy.as_view(), name='booking-detail'),
    path('menu/', views.MenuListCreate.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.MenuRetrieveUpdateDestroy.as_view(), name='menu-detail'),
]
