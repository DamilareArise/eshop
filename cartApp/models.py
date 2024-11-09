from django.db import models
from eshop.productApp.models import Product
from eshop.userApp.models import Profile

# Create your models here.

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def total_cost(self):
        return self.product.price * self.quantity


    

