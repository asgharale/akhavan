from django.db import models
import django_jalali.db.models as jmodels
from django_ckeditor_5.fields import CKEditor5Field

class DiscountGroup(models.Model):
    title = models.CharField(unique=True, max_length=100)
    meta = models.TextField(max_length=400, blank=True)
    amount = models.SmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.title + ' - ' + str(self.amount)

class Detail(models.Model):
    title = models.CharField(max_length=255)
    value = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.title

class IntDetail(models.Model):
    title = models.CharField(max_length=255)
    value = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    STATUSES = (
        ('T', "Published"),
        ('F', "Draft"),
        ('A', "Archived")
    )
    title = models.CharField(max_length=255)
    address = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to="store/products/%Y-%m", max_length=500, default="store/defaults/product.png")
    meta = models.TextField(max_length=400)
    stock_quantity = models.PositiveIntegerField(blank=True, null=True)
    images = models.ManyToManyField("mediastore.Image", blank=True)
    videos = models.ManyToManyField("mediastore.Video", blank=True)

    categories = models.ManyToManyField("sort.Category", blank=True)
    Tags = models.ManyToManyField("sort.Tag", blank=True)

    org_price = models.IntegerField(default=0)
    discount = models.SmallIntegerField(default=0)
    discount_group = models.ForeignKey(DiscountGroup, on_delete=models.DO_NOTHING)
    buyers = models.ManyToManyField("user.CUser", blank=True)

    details = models.ManyToManyField(Detail, blank=True)
    int_detail = models.ManyToManyField(IntDetail, blank=True)
    body = CKEditor5Field(blank=True, null=True, config_name='extends')

    status = models.CharField(max_length=1, choices=STATUSES, default='F')
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)

    @property
    def count_sell(self) -> int:
        return self.buyers.count()
    @property
    def is_exist(self) -> bool:
        if self.stock_quantity:
            return True
        return False

    def __str__(self):
        return self.address + ' - ' + self.title
    def get_sell_price(self):
        min = self.org_price * ((100-self.discount)/100)
        if self.discount_group:
            group_price = self.org_price * ((100-self.discount_group.amount)/100)
            if min>group_price:
                min = group_price
        return min
    def get_score(self):
        pass

class Review(models.Model):
    user = models.OneToOneField("user.CUser", on_delete=models.CASCADE, related_name="users")
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING, related_name="reviews")
    point = models.SmallIntegerField(default=0)
    comment = models.TextField(max_length=500)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' -ON- ' + self.product.title


class Ad(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title