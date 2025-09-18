from django.shortcuts import render

# Create your views here.
def index(requrest):
    return render(requrest,'index.html',{})