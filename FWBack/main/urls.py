from django.urls import path

from . import views


urlpatterns = [
    path('api/user/', views.user, name='user'),
    path(r'api/category/', views.categoryView, name='categoryV'),
    path(r'api/category/<int:pk>', views.category_detail, name='categoryD'),
    path(r'api/category/product/<int:pk>/', views.product_detail, name='productV'),
    ]