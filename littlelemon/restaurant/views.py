from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
