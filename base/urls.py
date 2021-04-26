from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('register/',views.RegisterPage.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('',views.TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',views.TaskDetail.as_view(),name='task'),
    path('create-task',views.TaskCreate.as_view(),name='create-task'),
    path('update-task/<int:pk>',views.TaskUpdate.as_view(),name='update-task'),
    path('delete-task/<int:pk>',views.DeleteTask.as_view(),name='delete-task'),
]