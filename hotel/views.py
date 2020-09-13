from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from hotel.models import Hotel


def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/index.html', {'hotels': hotels})

