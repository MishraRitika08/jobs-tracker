from django.db import models
# all the db related to this app are staying here 
# Create your models here.
# name of the schema is Student here

class Student(models.Model):
    #id = models.AutoField(primary_key=True) here this field is added automatically by django so we don't need to add it manually
    name = models.CharField(max_length= 100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null = True)

class Company(models.Model):
    name = models.CharField(max_length= 100)
    applied = models.BooleanField(default=False)

    def __str__(self):
        return self.name   

    