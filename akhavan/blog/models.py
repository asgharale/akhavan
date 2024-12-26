from django.db import models
import django_jalali.db.models as jmodels
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='P')


class Article(models.Model):
    STATUSES = (
        ('P', "Published"),
        ('D', "Draft"),
        ('A', "Archived")
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    address = models.SlugField(max_length=255, unique=True)
    meta = models.TextField(max_length=400)
    thumbnail = models.ImageField(upload_to="blog/thumbnails-%Y/", blank=True)
    categories = models.ManyToManyField("sort.Category", blank=True)
    tags = models.ManyToManyField("sort.Tag", blank=True)
    body = CKEditor5Field(blank=True, null=True, config_name='extends')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES, default='D')
    read_time = models.SmallIntegerField()
    views = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="viewed")
    created_at = jmodels.jDateField(auto_now_add=True)
    last_modified = jmodels.jDateField(auto_now=True)
    open_conv = models.BooleanField(default=True, verbose_name="Open Converstaion")    
    @property
    def likes_count(self):
        return self.likes.count()
    @property
    def views_count(self):
        return self.views.count()

    def __str__(self):
        return "%s - %s" % (self.title, self.address)
    class Meta:
        ordering = ('last_modified',)

    # managers
    objects = models.Manager()
    published = PublishedManager()



class Comment(models.Model):
    STATUSES = (
        ('P', "Published"),
        ('D', "Draft"),
    )

    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField(max_length=200)
    full_name = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    created_at = jmodels.jDateField(auto_now_add=True)
    status = models.CharField(max_length=1, default='D', choices=STATUSES)

    # managers
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return "%s - %s - %s" % (self.article.title, self.full_name, self.email)
