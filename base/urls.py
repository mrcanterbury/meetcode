from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("board/<uuid:pk>", views.board, name="board"),
]