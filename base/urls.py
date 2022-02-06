from django.urls import path
from . import views

urlpatterns = [
    path("user-register/", views.userRegister, name="user-register"),
    path("user-login/", views.userLogin, name="user-login"),
    path("user-logout/", views.userLogout, name="user-logout"),
    path("", views.home, name="home"),
    path("board/<str:pk>", views.board, name="board"),
    path("new-board/", views.newBoard, name="new-board"),
    path("edit-board/<str:pk>", views.editBoard, name="edit-board"),
    path("remove-board/<str:pk>", views.removeBoard, name="remove-board"),
    path("user-error/", views.userError, name="user-error"),
]