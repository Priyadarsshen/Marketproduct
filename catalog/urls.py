from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('Addproduct',views.Addproduct,name="Addproduct"),
    path('shop',views.shop,name="shop"),
    path('shop/<str:name>',views.shopview,name="shopview"),
    path('shop/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('update/<int:pk>',views.update,name="update"),
    path('delete/<int:pk>',views.delete,name="delete"),
]
