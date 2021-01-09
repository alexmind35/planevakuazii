from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    photo_executor = models.ImageField("Фото заказчика", upload_to="accounts/customer", default="", blank=True)

    def __str__(self):
        return "User: {}, org_name: {}, org_address: {}, phone: {}, photo_executor: {}".format(self.user, self.org_name,
                                                                                               self.org_address,
                                                                                               self.phone,
                                                                                               self.photo_executor)


class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_executor = models.ImageField("Фото исполнителя", upload_to="accounts/executor", default="", blank=True)

    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.photo_executor)
