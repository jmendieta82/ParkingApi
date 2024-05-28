from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
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
    queryset = Ticket.objects.all()
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
