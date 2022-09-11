from django.db import models


class Blog(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    published = models.DateTimeField(verbose_name='Дата и время публикации', auto_now_add=True)
    blog_text = models.TextField(verbose_name='Текст', max_length=1000)

    class Meta():
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'{self.title}, опубликован {self.published}'
