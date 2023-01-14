from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    # Product
    path('', index, name='home'),
    path('products', product_list_view, name='product-list'),
    #Category
    path('categories', category_list_view, name='category-list'),
    path('category/<cid>/', product_cat_wise, name='product-list-cat-wise'),
    # Vendor
    path('vendors', vendor_list, name='vendors-list'),
]
