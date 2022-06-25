# Generated by Django 4.0.5 on 2022-06-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('blogs', models.ManyToManyField(related_name='tags', to='blogs.blog', verbose_name='Блоги')),
            ],
        ),
    ]
