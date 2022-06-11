from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Добавляет второй ведущий
class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='слаг')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

# Добавляет первый ведущий
class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Поделитесь своими мыслями'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='group_post',
        blank=True, null=True,
        verbose_name='Сообщество',
        help_text='Выберите сообщество (необязательно)'
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]

# Добавляет третий ведущий
class Comment(models.Model):
    # Вначале создается модель без привязки к посту
    # post = models.ForeignKey(
    #     Post,
    #     on_delete=models.CASCADE,
    #     related_name='comments',
    # )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-created',)
