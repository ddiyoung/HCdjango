from django.contrib import admin

# Register your models here.
from hotel.models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image', 'pubDate', 'userRating')



