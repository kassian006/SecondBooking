from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'user_role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CountryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_name']


class CityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['city_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_images']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserProfileSimpleSerializer()

    class Meta:
        model = Review
        fields = ['user_name', 'text', 'parent', 'stars']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'room_status', 'room_price', 'room_images']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'hotel_room', 'room_type', 'room_status', 'room_price',
                  'all_inclusive', 'room_description', 'room_images']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    city = CityListSerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'address', 'hotel_stars', 'hotel_images', 'avg_rating',
                  'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountryListSerializer()
    owner = UserProfileSimpleSerializer()
    city = CityListSerializer()
    created_date = serializers.DateField(format('%d-%m-%Y'))
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)


    class Meta:
        model = Hotel
        fields = ['hotel_name', 'owner', 'hotel_description', 'country', 'city', 'address', 'hotel_stars',
                  'hotel_images', 'hotel_video', 'created_date', 'rooms', 'reviews']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class CountryDetailSerializer(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)
    # city = CityListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'hotels']


class CityDetailSerializer(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city_name', 'hotels']
