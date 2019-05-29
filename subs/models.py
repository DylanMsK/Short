from django.db import models

# Create your models here.
class Sub(models.Model):
    origin = models.TextField()
    new = models.TextField()

    def __str__(self):
        return f'{self.new}'