from django.db import models


# Create your models here.

class Memory(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
