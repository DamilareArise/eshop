from django.db import models
from eshop.userApp.models import Profile

# Create your models here.

class Product(models.Model):

    categories = [
        ('Clothings', 'Clothings'),
        ('Electronics', 'Electronics'),
        ('Home', 'Home')
    ]

    product_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,  null=True)
    image = models.ImageField(upload_to='product_image/', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30, choices=categories, null=True)
    


    def __str__(self) -> str:
        return self.title
    

   