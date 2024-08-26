from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
def look(request):
    return HttpResponse('Hello my name is Khurshed')

def kill(request):
    items = Person.objects.all()
    context = {
        'items':items
    }
    return render(request,'ice/index.html',context)

def itemsid(request,my_id):
    item = Person.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request,'ice/detail.html',context)