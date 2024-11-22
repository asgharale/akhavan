from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckefitor5/", include("django_ckeditor_5.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# admin side custom
admin.site.site_title = "اخوان مبل"
admin.site.site_header = "اخوان مبل پنل ادمین"
admin.site.index_title = "بلاگ نمونه ادمین ساید"
