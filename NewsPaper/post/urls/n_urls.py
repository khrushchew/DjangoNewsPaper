from django.urls import path

from post.views.list_view import ListPostView
from post.views.retrieve_view import RetrievePostView
from post.views.create_view import CreatePostView
from post.views.update_view import UpdatePostView
from post.views.delete_view import DeletePostView

urlpatterns = [
    path('', ListPostView.as_view(type_of_post='N')),
    path('<int:pk>/', RetrievePostView.as_view()),
    path('create/', CreatePostView.as_view(type_of_post='N')),
    path('<int:pk>/update/', UpdatePostView.as_view(type_of_post='N')),
    path('<int:pk>/delete/', DeletePostView.as_view(type_of_post='N'))
]
