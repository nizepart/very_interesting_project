from django.db import models
from django.contrib.auth.models import User
from places.fields import PlacesField


# Create your models here.

class Memory(models.Model):
    location = PlacesField('Место на карте')
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
