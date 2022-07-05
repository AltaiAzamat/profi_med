from django.db import models
from backend.apps.accounts.models import User
# Create your models here.
#
# class Category(models.Model):
#     name = models.CharField("название", max_length=50, unique=True)
#     slug = models.SlugField("слаг", max_length=60, unique=True)
#
#     class Meta:
#         verbose_name = "категория"
#         verbose_name_plural = "Специалисты"
#         ordering = ['name']
#     def __str__(self):
#         return self.name
#



# class Order(models.Model):
#     STATUS_NEW = "new"
#     STATUS_CONFIRMED = "confirmed"
#     STATUS_SEND = "send"
#     STATUS_DELIVERED = "delivered"
#     STATUS_REJECTED = "rejected"
#     ORDER_STATUSES = (
#         (STATUS_NEW, "Новый"),
#         (STATUS_CONFIRMED, "Подтвержден"),
#         (STATUS_SEND, "Отправлен"),
#         (STATUS_DELIVERED, "Доставлен"),
#         (STATUS_REJECTED, "Отменен"),
#     )
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     address = models.CharField("Адрес", max_length=255)
#     postal_code = models.CharField("Почтовый индекс", max_length=10)
#     mobile = models.CharField("Номер телефона", max_length=10)
#     notice = models.CharField("Комментарий", max_length=255)
#     status = models.CharField(
#         "Статус",
#         max_length=9,
#         choices=ORDER_STATUSES,
#         default=STATUS_NEW
#     )
#

class Articles(models.Model):
    title = models.CharField('Нaзвание', max_length = 50)
    anons = models.CharField("Анонс", max_length=250)
    image = models.ImageField("фото", upload_to="news_images/")
    full_text = models.TextField("Cтатья")
    date = models.DateTimeField("Дaта публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"