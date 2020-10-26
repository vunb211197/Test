from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('image_upload/',views.upload_image),
    path('image_upload/check_lp/<str:image_name>',views.check_lp,name = "check_lp"),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)