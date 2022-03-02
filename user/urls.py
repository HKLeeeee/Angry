from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.u_login, name='u_login'),
    path('signup/', views.u_signup, name='u_signup'),
    path('signupSuccess/', views.signup_success, name='signup_success'),
    path('loginProcess/', views.login_process, name='login_process'),
    path('logout/', views.u_logout, name='u_logout'),
    path('setting/', views.u_setting, name='u_setting')
]
