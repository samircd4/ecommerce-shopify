from django.shortcuts import render
from core.models import Product, Category, Tags, Vendor, CartOrder, CartOrderItems, ProductReview, Address, Wishlist, ProductImage


def index(request):
    products = Product.objects.filter(product_status='published').order_by('-id')
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status= 'published')
    
    context = {'products': products}
    
    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories":categories
    }
    return render(request, 'core/category-list.html', context)

def product_cat_wise(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter( product_status='published', category=category)
    
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'core/product-category-list.html', context)