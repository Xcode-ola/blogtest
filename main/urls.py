from django.urls import path
from .views import base, index, create, UserPost, update, delete, blogpost

urlpatterns = [
    path('link_test/', base, name="base"),
    path('', index.as_view(), name="index"),
    path('<int:pk>/', blogpost, name="blogpost"),
    path('create/', create.as_view(), name="create"),
    path('edit/<int:pk>/', update.as_view(), name="update"),
    path('<int:pk>/delete/', delete.as_view(), name="delete"),
    path('user/<username>/', UserPost.as_view(), name="public"),
]