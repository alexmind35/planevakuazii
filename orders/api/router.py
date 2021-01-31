from rest_framework.routers import DefaultRouter

from orders.api.viewsets import UserOrderViewSet, AdminServiceViewSet, AdminImageschemeViewSet

order_router = DefaultRouter()
order_router.register(r'orders', UserOrderViewSet, basename='orders')
order_router.register(r'admin/service', AdminServiceViewSet, basename='admin-service')
order_router.register(r'admin/imagescheme', AdminImageschemeViewSet, basename='admin-imagescheme')