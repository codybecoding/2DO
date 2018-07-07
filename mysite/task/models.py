from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task


# class UserToTask(models.Model):
#     user = models.ForeignKey(UserTask, on_delete=models.CASCADE, null=True, unique=False)
    