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


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ParkingSpotSerializer(ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
