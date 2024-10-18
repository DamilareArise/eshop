from django.urls import path
from .views import profileView, editProfile

urlpatterns = [
    path('profile/<int:id>/', profileView, name='profile'),
    path('edit-profile/<int:id>/', editProfile, name='edit-profile')
]
