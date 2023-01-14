from core.models import Category

def default(request):
    categories = Category.objects.all()
    cat1 = Category.objects.all()[:5]
    cat2 = Category.objects.all()[5:10]
    return {
        'categories': categories,
        'cat1': cat1,
        'cat2': cat2,
    }