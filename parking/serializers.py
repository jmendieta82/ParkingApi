from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from parking.models import *


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        user = Employee(
            email=validated_data['email'],
            username=validated_data['username'],
            is_staff=validated_data['is_staff'],
            identification=validated_data['identification'],
            phone=validated_data['phone'],
            direction=validated_data['direction'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarSerializer(ModelSerializer):
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(write_only=True, allow_null=True, queryset=Brand.objects.all(),
                                                  source='brand')

    class Meta:
        model = Car
        fields = '__all__'


class ParkingSpotSerializer(ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    car = CarSerializer(read_only=True)
    owner = OwnerSerializer(read_only=True)
    parking_spot = ParkingSpotSerializer(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(write_only=True, allow_null=True, queryset=Car.objects.all(),
                                                source='car')
    owner_id = serializers.PrimaryKeyRelatedField(write_only=True, allow_null=True, queryset=Owner.objects.all(),
                                                  source='owner')
    parking_spot_id = serializers.PrimaryKeyRelatedField(write_only=True, allow_null=True,
                                                         queryset=ParkingSpot.objects.all(), source='parking_spot')

    class Meta:
        model = Ticket
        fields = '__all__'
