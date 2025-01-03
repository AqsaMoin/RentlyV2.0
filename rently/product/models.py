from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from autoslug import AutoSlugField
from django.forms import ValidationError
from django.utils.timezone import now

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,unique=True,null=True,blank=True)

    def __str__(self):
        return self.username


class Product(models.Model):

    PRODUCT_CATEGORIES = [
    ('electronics', 'Electronics'),
    ('sports','Sports'),
    ('space','Space'),
    ('books', 'Books'),
    ('home', 'Home'),
    ('others', 'Others'),
]

    product_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product_name = models.CharField(blank=False,max_length=255)
    product_image = models.FileField(upload_to='image/')
    product_category = models.CharField(max_length=100,choices=PRODUCT_CATEGORIES,default='others')
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=9,decimal_places=3)
    product_slug = AutoSlugField(populate_from="product_name",unique=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name} by {self.product_owner.username}"
    

class Payment(models.Model):
    
    PAYMENT_STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('COMPLETED','Completed'),
        ('FAILED','Failed'),
    ]

    def generate_payment_slug(instance):
        return f"{instance.user.username}--{instance.payment_date}"

    payment_price = models.DecimalField(max_digits=10,decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    payment_date = models.DateField(auto_now_add=True)
    payment_status= models.CharField(max_length=20,choices=PAYMENT_STATUS_CHOICES,default='PENDING')
    payment_slug = AutoSlugField(populate_from=generate_payment_slug,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.payment_price <= 0:
            raise ValidationError("There is error in payment it should not be zero")

    def __str__(self):
        return f"{self.payment_price} by {self.user.username}"
    
    

class Renting(models.Model):
    RENTAL_STATUS_CHOICES = [
        ('ACTIVE','Active'),
        ('COMPLETED','Completed'),
        ('OVERDUE','Overdue'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rented_days = models.IntegerField()
    rental_start_date = models.DateTimeField()
    rental_end_date = models.DateTimeField()
    rental_status = models.CharField(max_length=20,choices=RENTAL_STATUS_CHOICES,default='ACTIVE')
    penalty = models.DecimalField(default=0.00,max_digits=9,decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_penalty(self):
        if now() > self.rental_end_date:
            overdue_days = (now()-self.rental_end_date).days
            return overdue_days * 100
        return 0
    
    def clean(self):
        if self.rental_end_date <= self.rental_start_date:
            raise ValidationError("Rental end date must be after start date")

    def __str__(self):
        return f"{self.product.product_name} rented by {self.user.username}"
    

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Cart of {self.user.username} with {self.products.count()} items"



class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wishlist of {self.user.username} with {self.products.count()} items"
    