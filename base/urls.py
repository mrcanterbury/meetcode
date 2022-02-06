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
    path("delete-board/<str:pk>", views.deleteBoard, name="delete-board"),
    path("delete-comment/<str:pk>", views.deleteComment, name="delete-comment"),
    path("user-error/", views.userError, name="user-error"),
]