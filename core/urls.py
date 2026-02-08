from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet,OrdersViewSet,ProductViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]