from django.db import models
from attr.validators import max_len
from debugpy.common import timestamp

# Create your models here.



class Message(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.username}: {self.content}"
    
    
    
    

