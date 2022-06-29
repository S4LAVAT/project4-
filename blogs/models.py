from django.db import models
from django.contrib.auth.models import User


TEXT_CAT ='tb'
MUSIC_CAT ='mb'
CAT_CHOICES=(
	(TEXT_CAT, 'Текстовый блог'),
	(MUSIC_CAT, 'Музыкальный блог')
)


class Blog(models.Model):
	text = models.TextField()
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.CharField( max_length=50, choices=CAT_CHOICES, default=TEXT_CAT)

	def __str__(self):
		return self.title


	class Meta:
		ordering = ['-id']


class Tag(models.Model):
	name  = models.CharField(max_length=20)
	blogs = models.ManyToManyField( Blog, verbose_name="Блоги", related_name='tags')

	 
	def __str__(self):
		return self.name 

