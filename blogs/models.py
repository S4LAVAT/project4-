from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	text = models.TextField()
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']


class Tag(models.Model):
	name  = models.CharField(max_length=20)
	blogs = models.ManyToManyField( Blog, verbose_name="Блоги", related_name='tags')
	 
	def __str__(self):
		return self.name 

