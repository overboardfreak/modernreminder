from django.db import models
from django.contrib.auth.models import User

class Checklist(models.Model):
    name = models.CharField(max_length=40)
    time = models.TimeField()
    day = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

