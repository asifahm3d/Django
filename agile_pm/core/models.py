from django.db import models

class Sprint(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('doing', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Risk(models.Model):
    description = models.CharField(max_length=255)
    probability = models.IntegerField()
    impact = models.IntegerField()
    mitigation = models.TextField()

    def __str__(self):
        return self.description


class QualityCheck(models.Model):
    criterion = models.CharField(max_length=200)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return self.criterion
