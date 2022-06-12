from django.db import models
from backend.apps.accounts.models import User

class Category(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("слаг", max_length=60, unique=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Специалисты"
        ordering = ['name']
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField("название", max_length=70, unique=True)
    slug = models.SlugField("слаг", max_length=80, unique=True)

    class Meta:
        verbose_name = "под категория"
        verbose_name_plural = "подкатегории"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Имя",max_length=225)
    descriptions = models.TextField("краткая биография")
    price = models.DecimalField("цена", max_digits=10,decimal_places=2)
    image = models.ImageField("фото", upload_to ="product_images/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory,on_delete= models.PROTECT,related_name="products")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("активный", default=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reviews")
    text = models.TextField("отзыв")
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField("активный", default=True)

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "ОТЗЫВы"
        ordering = ['-created']

    def __str__(self):
        return f'{self.id}'

class BanerImage(models.Model):
    image = models.ImageField(upload_to='baners/')
    add_link = models.URLField()
    name = models.CharField("название", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "картинка для  баннера"
        verbose_name_plural = "картинки для банеров"

    def __str__(self):
        return self.name

#
# class Images(models.Model):
#     model_img = models.ImageField(upload_to='static/img')
