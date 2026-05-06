from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-project/', views.create_project, name='create_project'),
    path('create-task/', views.create_task, name='create_task'),
    path('done/<int:task_id>/', views.mark_done, name='done'),
    path('logout/', views.logout_view, name='logout'),
]