from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('tasks/', views.tasks, name="tasks"),
    path('view_task/', views.viewTask, name="view_task"),
    path('update_status/', views.updateStatus, name="update_status"),

]
