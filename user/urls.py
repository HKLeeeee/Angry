from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.u_login, name='u_login'),
    path('signin/', views.u_signin, name='u_signin'),
    path('signinSuccess', views.signin_success, name='signin_success'),
    path('loginProcess/', views.login_process, name='login_process'),
    path('logout/', views.u_logout, name='u_logout')
]
