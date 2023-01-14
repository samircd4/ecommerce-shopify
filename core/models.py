from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauth.models import User

# Create your models here.
STATUS = (
    ('draft','Draft'),
    ('disabled','Disabled'),
    ('rejected','Rejected'),
    ('in-review','In-review'),
    ('published','Published'),
)

STATUS_CHOICE = (
    ('process','Processing'),
    ('shiped','Shiped'),
    ('delivered','Delivered'),
)

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', alphabet='abcdefghijklmnop1234567890')#catabc123d45e
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

class Tags(models.Model):
    pass
    
class Vendor(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='ven', alphabet='abcdefghijklmnop1234567890')
    
    title = models.CharField(max_length=100, default = 'I am a vendor')
    image = models.ImageField(upload_to=user_directory_path, default='vendor.jpg')
    description = models.TextField(null=True, blank=True, default='I am an ammezing vendor')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    address = models.CharField(max_length=100, default='Bottrish, Kishoreganj')
    contact = models.CharField(max_length=100, default='+880 1781 355 377')
    chat_res_time = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100, default='100')
    authenticate_rating = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')
    joined = models.DateField(auto_now_add=True, null= True, blank=True)
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        
    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prd', alphabet='abcdefghijklmnop1234567890')
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    
    title = models.CharField(max_length=100, default = 'I am a product')
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = models.TextField(null=True, blank=True, default='I am an ammezing product')
    
    price = models.DecimalField(max_digits=9999, decimal_places=2, default=100)
    old_price = models.DecimalField(max_digits=9999, decimal_places=2, default=120)
    
    spacifications = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    
    product_status = models.CharField(choices=STATUS, max_length=20, default="in-review")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    fetured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True, length=5, max_length=10, prefix='sku', alphabet='1234567890')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_parcentage(self):
        discount = (self.old_price-self.price)*100/self.old_price
        return discount

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product-images', default='product.jpg')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product images'
    



class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999, decimal_places=2, default=100)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(max_length=35, choices=STATUS_CHOICE, default='processing')
    sku = ShortUUIDField(null=True, blank=True, length=5, prefix="SKU", max_length=20, alphabet="abcdefgh12345")
    
    class Meta:
        verbose_name_plural = 'Crat Order'
    
    # def __str__(self):
    #     return self.user
    

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999, decimal_places=2, default=100)
    total = models.DecimalField(max_digits=9999, decimal_places=2, default=100)
    
    class Meta:
        verbose_name_plural = 'Cart Order Items'
    
    def order_image(self):
        return mark_safe('<img scr="/media/%s" width="50" height="50" />' % (self.image))
    
    def __str__(self):
        return self.order
    

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product Reviews'
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Wishlists'
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Addresses'
    
    def __str__(self):
        return self.address





