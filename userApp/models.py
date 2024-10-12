from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# address 
# date of birth
# gender
# profile picture 
# validIdCard
# proofOfRegistration
# state of origin
# country
# role => user, vendor, supervisor 


class Profile(models.Model):
    sex = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    ]

    role = [
        ('user', 'user'),
        ('vendor', 'vendor'),
        ('supervisor', 'supervisor'),
    ]


    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices= sex,  max_length=10, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    valid_id_card = models.ImageField(upload_to='id_cards/', null=True, blank=True)
    proof_of_registration = models.ImageField(upload_to='proof_of_registration/', null=True, blank=True)
    state_of_origin = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(choices=role, max_length=10, null=True, blank=True)

    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()