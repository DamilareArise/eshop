from django.urls import path
from .views import profileView, editProfile, alluserView, de_or_reactivateView

urlpatterns = [
    path('profile/<int:id>/', profileView, name='profile'),
    path('edit-profile/<int:id>/', editProfile, name='edit-profile'),
    path('all-user', alluserView, name='all-user'),
    path('de-activate/<int:id>/', de_or_reactivateView, name='de-activate')

]
