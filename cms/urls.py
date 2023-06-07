from django.contrib import admin
from django.urls import path
from cms import views

urlpatterns = [
    path('', views.index),
    path('addUser',views.addUser),
    path('addPost',views.addPost),
    path('addLike',views.addLike),
    path('getAll',views.getAll),
    path('getLikes',views.getLikes),
    path('getUser/<int:id>',views.getUser),
    path('getPost/<slug:id>',views.getPost),
    path('getLike/<int:id>',views.getLike),
    path('updateUser/<int:id>',views.updateUser),
    path('updatePost/<slug:id>',views.updatePost),
    path('updateLike/<int:id>',views.updateLike),
    path('deleteUser/<int:id>/delete',views.deleteUser),
    path('deletePost/<slug:id>/delete',views.deletePost),
    path('deleteLike/<int:id>/delete',views.deleteLike),



]
