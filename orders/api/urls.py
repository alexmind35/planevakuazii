from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from orders.views import OrderListView, OrderCreateView, OrderUpdateView, OrderRetrieveView, OrderDestroyView, \
    ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceRetrieveView, ServiceDestroyView, ImageschemeListView, \
    ImageschemeCreateView, ImageschemeUpdateView, ImageschemeRetrieveView, ImageschemeDestroyView, AdminServiceViewSet

router = DefaultRouter()
router.register(r'admin/service', AdminServiceViewSet, basename='admin-service')

router = SimpleRouter()
router.register('services/all', ServiceListView, basename='service-list')
router.register('services/create', ServiceCreateView, basename='service-create')
router.register('services/update/<int:pk>', ServiceUpdateView, basename='service-update')
router.register('services/detail/<int:pk>', ServiceRetrieveView, basename='service-detail')
router.register('services/delete/<int:pk>', ServiceDestroyView, basename='service-delete')

router.register('orders/all', OrderListView, basename='order-list')
router.register('orders/create', OrderCreateView, basename='order-create')
router.register('orders/update/<int:pk>', OrderUpdateView, basename='order-update')
router.register('orders/detail/<int:pk>', OrderRetrieveView, basename='order-detail')
router.register('orders/delete/<int:pk>', OrderDestroyView, basename='order-delete')

router.register('imagescheme/all', ImageschemeListView, basename='imagescheme-list')
router.register('imagescheme/create', ImageschemeCreateView, basename='imagescheme-create')
router.register('imagescheme/update/<int:pk>', ImageschemeUpdateView, basename='imagescheme-update')
router.register('imagescheme/detail/<int:pk>', ImageschemeRetrieveView, basename='imagescheme-detail')
router.register('imagescheme/delete/<int:pk>', ImageschemeDestroyView, basename='imagescheme-delete')

urlpatterns = [

]
urlpatterns += router.urls
