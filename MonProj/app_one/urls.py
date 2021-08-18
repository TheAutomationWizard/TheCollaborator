from django.urls import path
from . import views

app_name = 'app_one'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('index/', views.collaborator_login, name='index'),
    path('logout/', views.collaborator_logout, name='logout')
]