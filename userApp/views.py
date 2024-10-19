from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import SignUpForm,EditProfileForm, EditUserProfileForm, AdminProfileForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'

@login_required
def profileView(request, id): 
    myInfo = Profile.objects.get(user_id = id )
    # print(myInfo.user.email)
    # Select * from profile  => fetchall => [<object 1>, <object 2>]
    # Select * from profile where user_id = 1 => fetchall [<object 1>]
    # Select * from profile where user_id = 1 => fetchone <object 1>
    
    return render(request, template_name='userApp/profile.html', context={'profile':myInfo})

@login_required
def editProfile(request, id):
    userInfo = get_object_or_404(User, id = id)
    profileInfo = get_object_or_404(Profile, user_id = id)

    if request.method == 'POST':
        userForm = EditUserProfileForm(request.POST, request.FILES, instance=userInfo )
        if request.user.is_superuser:
            profileForm = AdminProfileForm(request.POST, request.FILES, instance=profileInfo )
        else:
            profileForm = EditProfileForm(request.POST, request.FILES, instance=profileInfo )

        if userForm.is_valid() and profileForm.is_valid():
            if profileForm.cleaned_data['role'].lower() == 'vendor':
                userInfo.is_staff = True
                userInfo.is_superuser = False
            elif profileForm.cleaned_data['role'].lower() == 'supervisor':
                userInfo.is_staff = True
                userInfo.is_superuser = True
            else:
                userInfo.is_staff = False
                userInfo.is_superuser = False

            userForm.save()
            profileForm.save()

            return redirect('profile', id)
        else:

            return render(request, template_name='userApp/edit_profile.html', context={'userForm':userForm, 'profileForm':profileForm})

    else:
        userForm = EditUserProfileForm(instance=userInfo)
        if request.user.is_superuser:
            profileForm = AdminProfileForm(instance=profileInfo)
        else:
            profileForm = EditProfileForm(instance=profileInfo)

        return render(request, template_name='userApp/edit_profile.html', context={'userForm':userForm, 'profileForm':profileForm})

@login_required
def alluserView(request):
    users = Profile.objects.all()

    return render(request, template_name='userApp/all_users.html', context={'users':users})

@login_required
def de_or_reactivateView(request, id):
    user = User.objects.get(id=id)
    if user.is_active:
        User.objects.filter(id=id).update(is_active = False)
    else:
        User.objects.filter(id=id).update(is_active = True)

    
    return redirect('profile', id)