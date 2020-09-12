from django.test import TestCase

from hotel.models import Hotel
# Create your tests here.


class HotelTestCase(TestCase):
    def test_add_new_hotel_case(self):
        h = Hotel(title='테넷', link = 'https://naver.com', image = 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1323/132345_P01_153355.jpg', pubDate='2001', userRating='10.00')
        h.save()

        assert h.title == '테넷' and h.link == 'https://naver.com' and h.image == 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1323/132345_P01_153355.jpg' and h.pubDate == '2001' and h.userRating == '10.00'