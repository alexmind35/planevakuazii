from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Название услуги", max_length=255)
    price = models.PositiveIntegerField("Цена")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


    def __str__(self):
        return f'User: {self.user}, name: {self.name}, price: {self.price}'


class Image(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image_scheme = models.ImageField("Изображение план-схемы", upload_to="orders/service")

    class Meta:
        verbose_name = "План-схема"
        verbose_name_plural = "План-схемы"

    def __str__(self):
        return "Service: {}, image_scheme: {}".format(self.service, self.image_scheme)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_order = models.DateTimeField("Дата создания заказа",auto_now_add=True)
    time_order = models.TimeField("Время создания заказа", auto_now_add=True)
    count_images = models.IntegerField("Количество план-схем")
    STATUS_ORDERS = [
        ('1', 'Новый'),
        ('2', 'Отменен'),
        ('3', 'Выполнен')
    ]
    status_order = models.CharField(choices=STATUS_ORDERS, default='1', max_length=1)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-date_order"]

    def __str__(self):
        return "Customer: {}, service: {}, date_order: {}, time_order: {}, status_orders: {}, count_images: {}".format(
            self.user,
            self.service,
            self.date_order,
            self.time_order,
            self.get_status_order_display(),
            self.count_images)
