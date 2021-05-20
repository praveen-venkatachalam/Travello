from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from travello.models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 100
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'The city of briyani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 500
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Chennai'
    dest3.desc = 'Marina is Gone'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Delhi'
    dest4.desc = 'Fort of India'
    dest4.img = 'destination_4.jpg'
    dest4.price = 400
    dest4.offer = False

    dests = [dest1, dest2, dest3, dest4]

    return render(request, 'index.html', {'dests':dests})