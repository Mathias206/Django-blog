from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.post_list, name='blog_list'),
    path('post/<int:pk>/', views.post_detail, name= 'post_detail'),
    path("post/new/", views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name= 'post_edit'),
    path('login/', views.user_login, name= 'user_login'),
    path('logout/', views.log_out_user, name= 'log_out_user'),
    path('register/', views.user_register, name= 'user_register')
]