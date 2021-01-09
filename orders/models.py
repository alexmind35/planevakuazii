from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField("Цена")

    def __str__(self):
        return f'User: {self.user}, name: {self.name}, price: {self.price}'


class Image(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image_scheme = models.ImageField("Изображение схемы", upload_to="orders/service")

    def __str__(self):
        return "Service: {}, image_scheme: {}".format(self.service, self.image_scheme)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    time_order = models.TimeField(auto_now_add=True)
    count_images = models.IntegerField()
    STATUS_ORDERS = [
        ('1', 'Новый'),
        ('2', 'Отменен'),
        ('3', 'Выполнен')
    ]
    status_order = models.CharField(choices=STATUS_ORDERS, default='1', max_length=1)

    def __str__(self):
        return "Customer: {}, service: {}, date_order: {}, time_order: {}, status_orders: {}, count_images: {}".format(
            self.user,
            self.service,
            self.date_order,
            self.time_order,
            self.get_status_order_display(),
            self.count_images)
