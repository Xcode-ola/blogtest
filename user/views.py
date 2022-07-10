from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import UserUpdateForm, ProfileUpdateForm
from main.models import Blog
from .models import Profile

# Create your views here.

def register(response):
    if response.method == 'POST':
        username = response.POST['username']
        email = response.POST['email']
        password = response.POST['password1']
        password2 = response.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(response, "This email already exists in our database")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(response, "This username already exists in our database")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #automatically login the new user
                user = auth.authenticate(username=username, password=password)
                auth.login(response, user)

                #instant profile creation for new user
                new_user = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=new_user)
                new_profile.save()
                return redirect('edit_profile')

        else:
            messages.info(response, "The passwords do not match")
            return redirect('register')

    else:
        return render(response, 'user/register.html')

def login(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(response, user)
            return redirect('profile_page')

        else:
            messages.info(response, "Invalid Credentials")
            return redirect('login')

    return render(response, 'registration/login.html')

def ProfileEdit(response):
    if response.method == "POST":
        u_form = UserUpdateForm(response.POST, instance=response.user)
        p_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile_page')

    else:
        u_form = UserUpdateForm(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.profile)

    form = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(response, 'user/edit_profile.html', form)

def ProfilePage(response):
    user_posts = Blog.objects.all()
    return render(response, 'user/profile_page.html', {'user_posts':user_posts})

def logout(response):
    auth.logout(response)
    return redirect('index')

