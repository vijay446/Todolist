from email.policy import default
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text