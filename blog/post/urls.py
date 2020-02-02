from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.home, name = "home"),
    path('post/<int:post_id>/', views.post, name = "post"),
    path('add-comment/<int:post_id>/', views.add_comment, name = "addcomment"),
    path('like/<int:post_id>', views.like, name = "like"),
    path('delete/<int:comment_id>', views.delete, name="delete"),
    path('all/', views.all, name = "all"),
    path('filter/', views.filter, name="filter"),
]
