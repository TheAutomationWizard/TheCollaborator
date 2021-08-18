from django.shortcuts import render
from . import forms
from .models import User_Authentication

# Create your views here.
def homepage(request):
    user_details = {'user': 'Aditya'}
    return render(request, 'app_one/homepage.html', context=user_details)


def login_page(request):
    return render(request, 'app_one/login_page.html')


def signup_page(request):
    form = forms.LoginForm()
    return render(request, 'app_one/signup_page.html', {'form': form})


def user_signin(request):
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print('form validated!')
            print(f"Password : {form.cleaned_data['password']}")

    return render(request, 'app_one/signup_page.html', {'form': form})


def login(request):

    form = forms.user_login()
    print(f'\n\n\nform = {form}\n\n\n')

    if request.method == 'POST':

        user_data = User_Authentication.objects.filter()
        print(f'\n\nUser Data : {user_data}\n\n')


        form = forms.user_login(request.POST)

        print(f'\n\n\nform2 = {form}\n\n\n')
        if form.is_valid():
            emailId_or_phone = None
            if form.cleaned_data.get('email'):
                emailId_or_phone = form.cleaned_data.get('email')
            else:
                emailId_or_phone = form.cleaned_data.get('phone')

            print(f'\n\n USerNAME : {emailId_or_phone}\n\n')


            password_db = User_Authentication.objects.filter(email=emailId_or_phone)
            if not password_db:
                password_db = User_Authentication.objects.filter(phone=emailId_or_phone)
            print(f'\n\n PWD : {password_db.value_list("password", flat=True)}\n\n')

            password = form.cleaned_data.get('password')

            return homepage(request)
        else:
            print('Error in form.')

    return render(request, 'app_one/signup_page.html', {'form': forms.LoginForm()})
