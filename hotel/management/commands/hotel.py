from django.core.management import BaseCommand
from hotel.models import Hotel
from datetime import datetime

import requests



class Command(BaseCommand):
    help = "hangang temperature collector"

    def handle(self, *args, **options):
        res = requests.get("http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList?key=321d10e609b727882f3cbd1c86dfa054&openStartDt=2015")
        data = res.json()['movieListResult']['movieList']
        for mo in data:
            hotel = Hotel(movieNm=mo['movieNm'],
                          openDt=mo['openDt'],
                          nationAlt=mo['nationAlt'],
                          repGenreNm=mo['repGenreNm'])
            hotel.save()