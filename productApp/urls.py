from django.urls import path
from .views import createProductView, allProductView, deleteProductView, editProductView


urlpatterns = [
    path('create-product/<int:userid>/', createProductView, name='create-product'),
    path('all-product/', allProductView, name='all-product'),
    path('delete-product/<int:prd_id>/', deleteProductView, name="delete-product"),
    path('edit-product/<int:prd_id>/', editProductView, name='edit-product')
]
