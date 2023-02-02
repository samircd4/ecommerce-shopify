from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    # Product
    path('', index, name='home'),
    path('products', product_list_view, name='product-list'),
    path('product/<pid>/', product_details, name='product-details'),
    #Category
    path('categories', category_list_view, name='category-list'),
    path('category/<cid>/', product_cat_wise, name='product-list-cat-wise'),
    # Vendor
    path('vendors', vendor_list, name='vendors-list'),
    path('vendor/<vid>/', vendor_details, name='vendor-details'),
    # Tags
    path('product/tag/<slug:tag_slug>/', tag_list, name='tags'),
]
