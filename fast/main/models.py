from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    surname= models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name