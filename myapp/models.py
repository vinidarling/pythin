from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    marks=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
    def str(self):
        return self.name



