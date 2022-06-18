from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


class Blog(models.Model):
    text = models.TextField() 
    title = models.CharField(max_length=50)
    created_date = models.DateField( auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    