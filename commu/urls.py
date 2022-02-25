

from django.urls import path,include
from commu import views
app_name = 'commu'
urlpatterns = [
    path('<int:media_id>/list/', views.b_list, name='b_list'),
    path('<int:media_id>/create/', views.b_create, name='b_create'),
    path('<int:board_id>/detail/', views.b_detail, name='b_detail'),
    path('<int:pk>/modify/', views.b_modify, name="b_modify")
]
