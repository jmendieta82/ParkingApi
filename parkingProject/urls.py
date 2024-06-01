from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parking.views import *

router = DefaultRouter()
router.register(r'employee', EmployeeView),
router.register(r'owner', OwnerView)
router.register(r'car', CarView)
router.register(r'parking_spot', ParkingSpotView)
router.register(r'tiket', TicketView)


urlpatterns = [
   path('api/', include(router.urls)),
   path('api/api-auth', ObtainTokenView.as_view(), name='api-auth'),
   path('api/searchByCel', SearchByCelView.as_view(), name='api-auth'),
]
