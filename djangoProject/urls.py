from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('djangoIIM.urls')),
    path('product' , include('djangoIIM.urls')),
    path('admin/', admin.site.urls),
]