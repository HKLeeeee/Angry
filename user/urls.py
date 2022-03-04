from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.u_login, name='u_login'),
    path('signup/', views.u_signup, name='u_signup'),
    path('signupSuccess/', views.signup_success, name='signup_success'),
    path('loginProcess/', views.login_process, name='login_process'),
    path('logout/', views.u_logout, name='u_logout'),
    path('set/', views.u_set, name='u_set'),
    path('nickChange/', views.nick_change, name='nick_change'),
    path('nickValid/', views.nick_valid, name='nick_valid'),
    path('delete/', views.u_delete, name='u_delete')
]
