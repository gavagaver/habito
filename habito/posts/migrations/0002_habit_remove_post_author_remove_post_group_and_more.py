# Generated by Django 4.1.1 on 2023-01-10 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Линк')),
                ('description', models.TextField(verbose_name='Описание')),
                ('complete_times', models.IntegerField(verbose_name='Количество выполнений')),
                ('complete_percent', models.IntegerField(verbose_name='Процент завершения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Название поста', max_length=200, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='post',
            name='habit',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to='posts.habit', verbose_name='Привычка'),
        ),
    ]
