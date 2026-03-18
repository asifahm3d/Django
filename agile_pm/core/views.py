from django.http import JsonResponse
from .models import Sprint, Task, Risk, QualityCheck

def sprint_list(request):
    return JsonResponse(list(Sprint.objects.values()), safe=False)

def task_list(request):
    return JsonResponse(list(Task.objects.values()), safe=False)

def risk_list(request):
    return JsonResponse(list(Risk.objects.values()), safe=False)

def quality_list(request):
    return JsonResponse(list(QualityCheck.objects.values()), safe=False)