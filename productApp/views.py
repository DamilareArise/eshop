from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateProductForm
from eshop.userApp.models import Profile
# Create your views here.

def displayProductVIew(request):
    products = Product.objects.all() 
    print(products)

    return render(request, template_name='index.html', context={'allproducts':products})


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