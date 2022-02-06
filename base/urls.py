from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginRegister, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    path("board/<str:pk>", views.board, name="board"),
    path("new-board/", views.newBoard, name="new-board"),
    path("edit-board/<str:pk>", views.editBoard, name="edit-board"),
    path("remove-board/<str:pk>", views.removeBoard, name="remove-board"),
]