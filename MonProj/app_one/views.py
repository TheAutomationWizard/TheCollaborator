from django.shortcuts import render
from django.urls import reverse

from . import forms
from .forms import LoginForm, UserForm, SignUpForm
from .models import User_Authentication

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    form = forms.LoginForm()
    return render(request, 'app_one/index.html', {'form': form})


def loginpage(request):
    return render(request, 'app_one/loginpage.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = SignUpForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = SignUpForm()

    return render(request, 'app_one/new_user_registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def collaborator_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def collaborator_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f'Username : {username} || Password {password}')
        collaborator = authenticate(username=username, password=password)

        if collaborator:
            if collaborator.is_active:
                login(request, collaborator)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NO LONGER ACTIVE !')

        else:
            print('Someone tried to login, but failed...')
            print(f'Username: {username}, Password : {password}')
            return HttpResponse('Login Details Invalid !')

    else:
        form = forms.LoginForm()
        return render(request, 'app_one/index.html', {'form': form})


def user_signin(request):
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print('form validated!')
            print(f"Password : {form.cleaned_data['password']}")

    return render(request, 'app_one/signup_page.html', {'form': form})


# def login(request):
#     form = forms.user_login()
#     print(f'\n\n\nform = {form}\n\n\n')
# 
#     if request.method == 'POST':
# 
#         user_data = User_Authentication.objects.filter()
#         print(f'\n\nUser Data : {user_data}\n\n')
# 
#         form = forms.user_login(request.POST)
# 
#         print(f'\n\n\nform2 = {form}\n\n\n')
#         if form.is_valid():
#             emailId_or_phone = None
#             if form.cleaned_data.get('email'):
#                 emailId_or_phone = form.cleaned_data.get('email')
#             else:
#                 emailId_or_phone = form.cleaned_data.get('phone')
# 
#             print(f'\n\n USerNAME : {emailId_or_phone}\n\n')
# 
#             password_db = User_Authentication.objects.filter(email=emailId_or_phone)
#             if not password_db:
#                 password_db = User_Authentication.objects.filter(phone=emailId_or_phone)
#             print(f'\n\n PWD : {password_db.value_list("password", flat=True)}\n\n')
# 
#             password = form.cleaned_data.get('password')
# 
#             return index(request)
#         else:
#             print('Error in form.')
# 
#     return render(request, 'app_one/index.html', {'form': forms.LoginForm()})
