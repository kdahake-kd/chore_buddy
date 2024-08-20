from django.urls import path
from api import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# urlpatterns = [
#     path('',views.HomeView.as_view(),name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.CustomLoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#     path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
#     path('task/new/', views.TaskCreateView.as_view(), name='task-create'),
#     path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-update'),
#     path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
#     path('tasks',views.TaskListView.as_view(),name='task-list'),
# ]



urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/confirm-delete/', views.TaskDeleteConfirmView.as_view(), name='task-confirm-delete'),
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('calendar/', views.calendar_view, name='calendar'),
   
    
]



