from django.urls import path

from orders.views import OrderListView, OrderCreateView, OrderUpdateView, OrderRetrieveView, OrderDestroyView, \
    ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceRetrieveView, ServiceDestroyView, ImageschemeListView, \
    ImageschemeCreateView, ImageschemeUpdateView, ImageschemeRetrieveView, ImageschemeDestroyView

urlpatterns = [
    path('services/all', ServiceListView.as_view()),
    path('services/create', ServiceCreateView.as_view()),
    path('services/update/<int:pk>', ServiceUpdateView.as_view()),
    path('services/detail/<int:pk>', ServiceRetrieveView.as_view()),
    path('services/delete/<int:pk>', ServiceDestroyView.as_view()),

    path('orders/all', OrderListView.as_view()),
    path('orders/create', OrderCreateView.as_view()),
    path('orders/update/<int:pk>', OrderUpdateView.as_view()),
    path('orders/detail/<int:pk>', OrderRetrieveView.as_view()),
    path('orders/delete/<int:pk>', OrderDestroyView.as_view()),

    path('imagescheme/all', ImageschemeListView.as_view()),
    path('imagescheme/create', ImageschemeCreateView.as_view()),
    path('imagescheme/update/<int:pk>', ImageschemeUpdateView.as_view()),
    path('imagescheme/detail/<int:pk>', ImageschemeRetrieveView.as_view()),
    path('imagescheme/delete/<int:pk>', ImageschemeDestroyView.as_view()),
]
