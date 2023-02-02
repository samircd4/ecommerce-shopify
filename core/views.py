from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from taggit.models import Tag
from core.models import Product, Category, Tags, Vendor, CartOrder, CartOrderItems, ProductReview, Address, Wishlist, ProductImage


def index(request):
    products = Product.objects.filter(product_status='published', status=True).order_by('-id')
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status= 'published', status=True)
    
    context = {'products': products}
    
    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(product_status= 'published', status=True)[:4]

    context = {
        "categories":categories,
        'products': products,
    }
    return render(request, 'core/category-list.html', context)

def product_cat_wise(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter( product_status='published', category=category, status=True)
    
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

def vendor_details(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor,product_status='published', status=True)
    categories = Category.objects.all()
    contex = {
        'vendor': vendor,
        'products': products,
        'categories': categories,
    }
    return render(request, 'core/vendor-details.html', contex)

def product_details(request, pid):
    product = Product.objects.get(pid=pid)
    p_images = product.p_images.all()
    categories = Category.objects.all()
    try:
        address = Address.objects.get(user = request.user)
    except:
        address = 'Address not found'
    products = Product.objects.filter(category = product.category).exclude(pid=pid)[:4]
    context = {
        'product': product,
        'p_images': p_images,
        'categories': categories,
        'address': address,
        'products': products,
    }
    return render(request, 'core/product-details.html', context)

def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status='published', status=True).order_by('-date')
    tags = Tag.objects.all()[:5]
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        products = products.filter(tags__in=[tag])
    context = {
        'products': products,
        'tag': tag,
        'tags': tags,
    }
    return render(request, 'core/tag.html', context)