from django.shortcuts import render
from .models import Menu,Booking
from .serilaizers import menuSerializer,bookingSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(requrest):
    return render(requrest,'index.html',{})


class MenuItemsView(ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=menuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=menuSerializer
    lookup_field='pk'

class BookingViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=bookingSerializer