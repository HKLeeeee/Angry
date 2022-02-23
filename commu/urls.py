

from django.urls import path,include
from commu import views
app_name=''
urlpatterns = [
    path('list/',views.b_list, name ='b_list'),
]
