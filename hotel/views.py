from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hotel.models import Hotel
# Create your views here.


def index(request):
    hotel = Hotel.objects.all()
    hotels = []

    for value in hotel:
        hotels.append({
            'id': value.id,
            'title': value.title,
            'link': value.link,
            'image': value.image,
            'pubDate': value.pubDate,
            'userRating': value.userRating,
        })
    return render(request, 'hotel/index.html', {'hotels': hotels})


'''
JsonResponse({
        'hotels': hotels
    }, json_dumps_params={'ensure_ascii': False})
'''
