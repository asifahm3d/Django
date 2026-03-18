from django.urls import path
from .views import sprint_list, task_list, risk_list, quality_list

urlpatterns = [
    path('sprints/', sprint_list),
    path('tasks/', task_list),
    path('risks/', risk_list),
    path('quality/', quality_list),
]