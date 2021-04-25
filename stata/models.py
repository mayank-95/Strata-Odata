from django.db import models
from django.http import HttpResponse


# Create your models here.


class Person(models.Model):
    UserName=models.CharField(max_length=200,unique=True)
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)
    MiddleName=models.CharField(max_length=200)
    Gender=models.CharField(max_length=15)
    Age=models.IntegerField(default=0)

class City(models.Model):
    Name = models.CharField(max_length=200)
    CountryRegion=models.CharField(max_length=200)
    Region=models.CharField(max_length=200)


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    address=models.CharField(max_length=300)


class Email(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)








