from django.db import models
from django.urls import reverse

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a make (e.g. Toyota)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('autos:all')

class Auto(models.Model):
    nickname = models.CharField(max_length=200)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('autos:all')