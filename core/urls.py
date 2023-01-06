from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('products', product_list_view, name='product-list'),
    path('category', category_list_view, name='category-list'),
    path('category/<cid>/', product_cat_wise, name='product-list-cat-wise'),
]
