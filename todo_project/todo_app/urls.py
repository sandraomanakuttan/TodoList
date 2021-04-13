from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.task_view,name="task_view"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("clear/",views.clear_all,name="clear"),
    path("update/<int:id>",views.update,name="update"),
    path("taskview/",views.TaskListView.as_view(),name="taskview"),
    path("taskdetail/<int:pk>/",views.TaskDetailView.as_view(),name="taskdetail"),
    path("taskupdate/<int:pk>/",views.TaskUpdateView.as_view(),name="taskupdate"),
    path("taskdelete/<int:pk>/",views.TaskDeleteView.as_view(),name="taskdelete")
]