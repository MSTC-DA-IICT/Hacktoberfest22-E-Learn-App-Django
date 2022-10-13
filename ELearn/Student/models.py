from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class StudentModel(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    joining_date = models.DateField(default=date.today)
    student_idnum = models.IntegerField()
    
    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name