from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<slug:slug>',views.posts,name='posts'),
    path('single-post/',views.single_post,name='post-details')
]