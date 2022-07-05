from django.db import models
from backend.apps.accounts.models import User
from backend.apps.product.models import *
# Create your models here.
class Gallery(models.Model):
    name = models.CharField("Имя",max_length=225)
    image = models.ImageField("фото", upload_to="product_images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

    def __str__(self):
        return self.name


class Zapis(models.Model):
    name = models.CharField("Имя",max_length=225)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name="products")
    is_active = models.BooleanField("активный", default=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.name

class SignIn(models.Model):
    name = models.CharField("ФИО",max_length=25)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="Выберите услугу")
    mobile = models.CharField("Номер телефона", max_length=11)
    # is_paid = models.BooleanField("оплачено", default=False)
    message = models.CharField("Пожелание \ сообщения", max_length=250)
    date = models.DateField("Дата")
    time = models.TimeField("Время")