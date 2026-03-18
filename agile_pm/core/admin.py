from django.contrib import admin
from .models import Sprint, Task, Risk, QualityCheck

admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(Risk)
admin.site.register(QualityCheck)
