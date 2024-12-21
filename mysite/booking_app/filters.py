from django_filters import FilterSet
from .models import Hotel, Room


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country':['exact'],
            'city': ['exact'],
            'hotel_stars': ['gt', 'lt']
        }

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_number':['exact'],
            'room_type': ['exact'],
            'room_status': ['exact'],
            'room_price': ['gt', 'lt'],
        }
