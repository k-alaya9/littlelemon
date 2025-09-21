from django.shortcuts import render
from .models import Menu
from .serilaizers import menuSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

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