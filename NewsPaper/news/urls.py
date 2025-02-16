from django.urls import path

from news.views.list_view import ListNewsView
from news.views.retrieve_view import RetrieveNewsView

urlpatterns = [
    path('', ListNewsView.as_view()),
    path('<int:pk>/', RetrieveNewsView.as_view())
]