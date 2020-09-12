from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hotel.models import Hotel
# Create your views here.


def index(request):
    hotel = Hotel.objects.all()
    hotels = []
    count = 0

    for value in hotel:
        count += 1
        """
        hotels.append(value.id)
        hotels.append(value.movieNm)
        hotels.append(value.openDt)
        hotels.append(value.nationAlt)
        hotels.append(value.repGenreNm)
        """
        hotels.append({
            'id': value.id,
            'movieNm': value.movieNm,
            'openDt': value.openDt,
            'nationAlt': value.nationAlt,
            'repGenreNm': value.repGenreNm,
            'count': count
        })

    return render(request, 'hotel/index.html', {'hotels': hotels},)


'''JsonResponse({
        'hotels': hotels
    }, json_dumps_params={'ensure_ascii': False})'''
