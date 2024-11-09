from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateProductForm
from eshop.userApp.models import Profile
# Create your views here.

def displayProductVIew(request):
    products = Product.objects.all() 
    print(products)

    return render(request, template_name='index.html', context={'allproducts':products})


def allProductView(request):
    products = Product.objects.all()
    return render(request, template_name='productApp/allproducts.html', context={'allproducts':products})


def createProductView(request, userid):
    created_by = Profile.objects.get(user_id = userid) 
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            createForm = form.save(commit=False)
            createForm.vendor = created_by
            createForm.save()

            return redirect('home')
        else:
            return render(request, template_name='productApp/create_product.html', context={'productForm':form})

    else:
        form = CreateProductForm()
        
        return render(request, template_name='productApp/create_product.html', context={'productForm':form})
    

def deleteProductView(request, prd_id):
    product = Product.objects.get(product_id=prd_id)
    product.delete()

    return redirect("all-product")


def editProductView(request, prd_id):
    product = Product.objects.get(product_id=prd_id)

    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save() 
            return redirect('all-product')
        else:
           return render(request, template_name="productApp/edit_product.html", context={"editForm":form}) 

    else:
        form = CreateProductForm(instance=product)
        return render(request, template_name="productApp/edit_product.html", context={"editForm":form})