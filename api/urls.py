from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview , name='api-overview'),
    path('task-list/', views.tasklist, name='task-list'),
    path('task-detale/<int:pk>', views.taskdetale, name='task-detale'),
    path('task-create/', views.taskcreat, name='task-create'),
    path('task-update/<int:pk>', views.taskupdate, name='task-update'),
    path('task-delete/<int:pk>', views.taskdelete, name='task-delete'),
]