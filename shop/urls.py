from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_list, name='category'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
]