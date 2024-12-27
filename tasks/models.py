from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name



class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=56)
    description = models.TextField(max_length=256, null=True, blank=True)


    def __str__(self):
        return f'{self.title}: {self.description}'   
