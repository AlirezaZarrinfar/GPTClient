from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    send = models.TextField()
    response = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    class Meta:
        db_table = "chat"