from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    name_service = models.CharField("Название услуги", max_length=255)
    price = models.PositiveIntegerField("Цена")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


    def __str__(self):
        return f'Услуга: {self.name_service}, цена: {self.price}'



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
        return "Пользователь: {}, {}, дата создания: {}, время создания: {}, статус: {}, количество схем: {}".format(
            self.user,
            self.service,
            self.date_order,
            self.time_order,
            self.get_status_order_display(),
            self.count_images)


class Imagescheme(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    image_plan_scheme = models.ImageField("Изображение план-схемы", upload_to="orders/imagescheme")

    class Meta:
        verbose_name = "План-схема"
        verbose_name_plural = "План-схемы"

    def __str__(self):
        return "Заказ: {}, изображение: {}".format(self.order, self.image_plan_scheme)