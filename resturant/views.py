from django.shortcuts import render
from .models import Menu,Booking
from .serilaizers import menuSerializer,bookingSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(requrest):
    return render(requrest,'index.html',{})


class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class=menuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class=menuSerializer
    lookup_field='pk'

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Booking.objects.all()
    serializer_class=bookingSerializer