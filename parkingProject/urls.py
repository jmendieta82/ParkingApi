from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parking.views import *

router = DefaultRouter()
router.register(r'employee', EmployeeView),
router.register(r'owner', OwnerView)
router.register(r'car', CarView)
router.register(r'brand', BrandView)
router.register(r'parking_spot', ParkingSpotView)
router.register(r'tiket', TicketView, basename='tiket')


urlpatterns = [
   path('api/', include(router.urls)),
   path('api/api-auth', ObtainTokenView.as_view(), name='api-auth'),
   path('api/searchByCel', SearchByCelView.as_view(), name='api-auth'),
   path('api/searchByPlate', SearchByPlateView.as_view(), name='api-auth'),
]
