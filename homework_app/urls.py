from django.urls import path
from .views import SubTaskListCreateView, SubTaskDetailSerializer, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]
