

from django.urls import path,include
from commu import views

app_name = 'commu'
urlpatterns = [
    path('<int:media_id>-<slug:category>/list/', views.b_list, name='b_list'),
    path('<int:media_id>-<slug:category>/create/', views.b_create, name='b_create'),
    path('<int:media_id>-<slug:category>/<int:board_id>/detail/', views.b_detail, name='b_detail'),
    path('<int:media_id>-<slug:category>/<int:board_id>/modify/', views.b_modify, name="b_modify"),
    path('<int:media_id>-<slug:category>/<int:board_id>/delete/', views.b_delete, name='b_delete'),
    path('<int:media_id>-<slug:category>/<int:board_id>/comment', views.create_comment, name='create_comment'),
    path('commentDelete/', views.comment_delete, name='comment_delete'),
    path('like/', views.b_like, name='b_like'),

]
