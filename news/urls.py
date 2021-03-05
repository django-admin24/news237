from django.urls import path
from .views import *
from .views import AddPost, UpdatePost, PostDeleteView

app_name = "news"

urlpatterns = [
   path('', homeview, name="home"),
   path('post/add/', AddPost.as_view(), name="add"),
   path('post/update/<slug>', UpdatePost.as_view(), name="post_update"),
   path('post/detail/<slug>', post_detail, name="post_detail"),
   path('post/category/<slug>', cat_view, name="category-detail"),
   path('post/<slug>/delete/', PostDeleteView.as_view(template_name='news/post_delete.html'), name='post-delete'),
   path('post/search/result', search, name="search"),
   path('post/<id>/user/', userpage, name='user-posts'),
   path('contact-us/', contact, name='contact'),
]
