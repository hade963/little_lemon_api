from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MenuitemsView(generics.ListCreateAPIView):
  queryset= Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuitemView (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset= Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet (viewsets.ModelViewSet):
  queryset= Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes= [IsAuthenticated]
