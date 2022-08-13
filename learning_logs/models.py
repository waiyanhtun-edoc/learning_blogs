# from operator import mod
# from cgitb import text
# from dataclasses import dataclass
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic of user learning about."""
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """Return string represendtion of model"""
        return self.text


class Entry(models.Model):
    """Something specific learned about topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    

    def __str__(self):
        """Returning string representation the models"""
        return f"{self.text[:50]}..."