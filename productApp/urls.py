from django.urls import path
from .views import createProductView


urlpatterns = [
    path('create-product/<int:userid>/', createProductView, name='create-product')
]
