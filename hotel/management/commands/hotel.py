from django.core.management import BaseCommand
from hotel.models import Hotel
from datetime import datetime

import requests



class Command(BaseCommand):
    help = "MOVIE COLLECTOR"

    def handle(self, *args, **options):
        headers = {'Content-Type': 'plain/text', 'X-Naver-Client-Id': 'L7fdgHlj4mgWbysxowRw', 'X-Naver-Client-Secret': 'fUtZiApJSR'}
        res = requests.get("https://openapi.naver.com/v1/search/movie?query=starwars&display=100&start=1&genre=&country=&yearfrom=1980&yearto=2020", headers=headers)
        data = res.json()['items']
        for mo in data:
            hotel = Hotel(
                title=mo['title'],
                link=mo['link'],
                image=mo['image'],
                pubDate=mo['pubDate'],
                userRating=mo['userRating'])
            hotel.save()