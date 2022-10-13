from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class TeacherModel(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    joining_date = models.DateField(default=date.today)
    teacher_idnum = models.IntegerField()

    