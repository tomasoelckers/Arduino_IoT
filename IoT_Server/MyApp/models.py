from django.db import models

class dataSensor(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.name
