from django.db import models

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name