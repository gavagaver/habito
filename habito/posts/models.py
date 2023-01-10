from django.db import models
from django.contrib.auth import get_user_model
from core.models import CreatedModel

User = get_user_model()
TITLE_CHAR_COUNT: int = 15


class Habit(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    slug = models.SlugField(verbose_name='Линк', unique=True)
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='Автор',
    )
    complete_times = models.IntegerField(verbose_name='Количество выполнений')
    complete_percent = models.IntegerField(verbose_name='Процент завершения')

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        default='Название поста',
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='Привычка',
        default=10,
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='posts/',
        blank=True,
    )

    def __str__(self):
        return f'{self.text[:TITLE_CHAR_COUNT] + "..."}'

    class Meta:
        ordering = ('-pub_date',)


class Comment(CreatedModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст нового комментария',
    )

    def __str__(self):
        return f'{self.text[:TITLE_CHAR_COUNT] + "..."}'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )
