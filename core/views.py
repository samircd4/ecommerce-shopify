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
    products = Product.objects.filter(product_status= 'published')[:4]

    context = {
        "categories":categories,
        'products': products,
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

def vendor_list(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors,
    }
    return render(request, 'core/vendors-list.html', context)