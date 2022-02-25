

from django.urls import path,include
from commu import views
app_name = 'commu'
urlpatterns = [
    path('<int:media_id>/list/', views.b_list, name='b_list'),
    path('<int:media_id>/create/', views.b_create, name='b_create'),
    path('<int:media_id>/<int:board_id>/detail/', views.b_detail, name='b_detail'),
    path('<int:media_id>/<int:board_id>/modify/', views.b_modify, name="b_modify"),
    path('<int:board_id>/delete/', views.b_delete, name='b_delete'),

]
