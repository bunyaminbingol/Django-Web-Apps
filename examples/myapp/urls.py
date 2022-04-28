from django.urls import path
from . import views

# http://127.0.0.1:8000         => index
# http://127.0.0.1:8000/details => details
# http://127.0.0.1:8000/list    => list

urlpatterns = [
    path('', views.index, name='products'),
    path('index', views.index),
    path('create', views.create),
    path('edit/<int:id>', views.edit, name="product_edit"),
    path('delete/<int:id>', views.delete, name="product_delete"),
    path('list', views.list, name="product_list"),
    path('upload', views.upload, name="upload_image"),
    path('<slug:slug>', views.details, name="product_details"),
]