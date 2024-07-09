from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from parking.serializers import *
from rest_framework.authtoken.models import Token


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class OwnerView(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ParkingSpotView(ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer


class TicketView(ModelViewSet):
    def get_queryset(self):
        queryset = Ticket.objects.filter(parking_spot__is_occupied=False)
        return queryset
    serializer_class = TicketSerializer


class ObtainTokenView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Remove previous tokens of the user
        Token.objects.filter(user=user).delete()
        # Create a new token for the user
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = EmployeeSerializer(user)
        return Response(usuario.data)


class SearchByCelView(APIView):
    def post(self, request):
        data = request.data
        phone = data['phone']
        owners = Owner.objects.filter(
            phone_number__contains=phone
        )
        owners_serializer = OwnerSerializer(owners, many=True)
        return Response(owners_serializer.data, status=status.HTTP_200_OK)


class SearchByPlateView(APIView):
    def post(self, request):
        data = request.data
        plate = data['plate']
        cars = Car.objects.filter(
            license_plate__contains=plate
        )
        cars_serializer = CarSerializer(cars, many=True)
        return Response(cars_serializer.data, status=status.HTTP_200_OK)

class BrandView(ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer
