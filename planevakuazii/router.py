from rest_framework.routers import DefaultRouter

from orders.api.viewsets import AdminOrderViewSet, UserOrderViewSet, AdminServiceViewSet, AdminImageschemeViewSet

router = DefaultRouter()
router.register(r'admin/order', AdminOrderViewSet, basename='admin-order')
router.register(r'user/order', UserOrderViewSet, basename='user-order')
router.register(r'admin/service', AdminServiceViewSet, basename='admin-service')
router.register(r'admin/imagescheme', AdminImageschemeViewSet, basename='admin-imagescheme')

