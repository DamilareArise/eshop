from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import SignUpForm,EditProfileForm, EditUserProfileForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'


def profileView(request, id): 
    myInfo = Profile.objects.get(user_id = id )
    # print(myInfo.user.email)
    # Select * from profile  => fetchall => [<object 1>, <object 2>]
    # Select * from profile where user_id = 1 => fetchall [<object 1>]
    # Select * from profile where user_id = 1 => fetchone <object 1>
    
    return render(request, template_name='userApp/profile.html', context={'profile':myInfo})


def editProfile(request, id):
    userInfo = get_object_or_404(User, id = id)
    profileInfo = get_object_or_404(Profile, user_id = id)

    if request.method == 'POST':
        userForm = EditUserProfileForm(request.POST, request.FILES, instance=userInfo )
        profileForm = EditProfileForm(request.POST, request.FILES, instance=profileInfo )

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()

            return redirect('profile', id)
        else:

            return render(request, template_name='userApp/edit_profile.html', context={'userForm':userForm, 'profileForm':profileForm})

    else:
        userForm = EditUserProfileForm(instance=userInfo)
        profileForm = EditProfileForm(instance=profileInfo)

        return render(request, template_name='userApp/edit_profile.html', context={'userForm':userForm, 'profileForm':profileForm})