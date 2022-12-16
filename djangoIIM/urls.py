from django.urls import path
from . import views

app_name = 'djangoIIM'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<id>', views.product, name='product'),
    path('<id>/update', views.update, name='update'),
    path('<id>/delete', views.delete, name='delete'),
]