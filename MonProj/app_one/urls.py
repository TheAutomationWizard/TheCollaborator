from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_page, name='signuppage'),
    path('login/', views.login_page, name='loginpage'),
    path('homepage/', views.homepage, name='homepage'),
    # path('signin/', views.user_signin, name='signin'),
    path('signin/', views.login, name='signin')
]