from django.utils import timezone
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор объявления', **NULLABLE)

    title = models.CharField(max_length=200, verbose_name='Название товара')
    image = models.ImageField(upload_to='ads/', verbose_name='Фото товара', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    description = models.TextField(verbose_name='Описание товара', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата и время создания объявления')

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление, под которым оставлен отзыв',
                           **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отзыва', **NULLABLE)

    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата и время создания отзыва')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
