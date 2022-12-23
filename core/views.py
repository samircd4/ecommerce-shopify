from django.shortcuts import render
from core.models import Product, Category, Tags, Vendor, CartOrder, CartOrderItems, ProductReview, Address, Wishlist, ProductImage


def index(request):
    products = Product.objects.filter(product_status='published').order_by('-id')
    context = {
        'products': products,
    }
    return render(request, 'core/index.html', context)
