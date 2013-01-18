from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, related_name='chatuser', blank=True)

    class Meta:
        verbose_name_plural = "Messages"
        ordering = ['-date']

    def __unicode__(self):
        return self.text