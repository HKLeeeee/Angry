

from django.urls import path,include
from commu import views
app_name='commu'
urlpatterns = [

    path('list/', views.b_list, name='b_list'),
    path('create/', views.b_create, name='b_create'),
    path('<int:board_id>/detail/',views.b_detail,name='b_detail'),
    path('<int:pk>/modify/',views.b_modify,name="b_modify")
]
