from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title