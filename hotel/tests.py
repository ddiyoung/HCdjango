from django.test import TestCase

from hotel.models import Hotel
# Create your tests here.


class HotelTestCase(TestCase):
    def test_add_new_hotel_case(self):
        h = Hotel()
