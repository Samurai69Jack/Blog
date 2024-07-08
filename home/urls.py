from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('blog_details/<int:blog_id>/',views.blog_details,name='blog_details'),
    path('edit_blog/<int:blog_id>/',views.edit_blog,name='edit_blog'),
    path('delete_blog<int:blog_id>/',views.delete_blog,name='delete_blog'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register_user,name='register'),
    path('your_blogs/',views.your_blogs,name='your_blogs'),
]