from django.urls import path

from profile.views.index_view import IndexProfileView

urlpatterns = [
    path('', IndexProfileView.as_view()),
]