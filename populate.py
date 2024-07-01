import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakerproject.settings')
django.setup()
from faker import Faker
from myapp.models import student
f=Faker()
def generate_data(n):
    for i in range(20):
        fname=f.name()
        froll=f.random_int(min=1,max=100)
        fmarks=f.random_int(min=1,max=100)
        fdob=f.date_of_birth()
        femail=f.email
s=student.objects.get_or_create(name=fname,roll=froll,marks=fmarks,dob=fdob,email=femail)
generate_data(20)
