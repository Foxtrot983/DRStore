from django.urls import path

from . import views


urlpatterns = [
   # path('api/user/', views.user, name='user'),
    path(r'api/category/', views.categoryView),
    path(r'api/category/<int:pk>', views.category_detail),
    path(r'api/product/', views.productView),
    path(r'api/product/<int:pk>', views.product_detail),
    ]