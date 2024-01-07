from django.urls import path,reverse_lazy
from .views import CustomLoginView, CustomLoguotView, RegisterPage, TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name= 'login'),
    path('logout/', CustomLoguotView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(),name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    path('', TaskList.as_view(), name='tasks'),
]