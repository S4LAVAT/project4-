from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    photo = models.ImageField (upload_to='user_images') 
    birth_date = models.DateField()
    bio = models.TextField()
    education = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
