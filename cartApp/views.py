from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from eshop.productApp.models import Product
from eshop.userApp.models import Profile
# Create your views here.

def allCart(request, userId):
    cart = Cart.objects.filter(user_id = userId) 

    return render(request, template_name="cartApp/cart.html", context={'cart':cart})


def addToCart(request, productId):
    product = get_object_or_404(Product, product_id = productId)
    user = get_object_or_404(Profile, user_id = request.user.id)
    
    Cart.objects.create(product = product, user = user)

    return redirect('cart', request.user.id)

def addQuantity(request, cartId):
    cart = get_object_or_404(Cart, cart_id = cartId)
    cart.quantity += 1
    cart.save()

    return redirect('cart', request.user.id)