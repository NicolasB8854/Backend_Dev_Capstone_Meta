from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
        
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer