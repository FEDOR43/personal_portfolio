from django.db import models


class Project(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=255)
    image = models.ImageField(verbose_name='Изображение', upload_to='portfolio/images/')
    url = models.URLField(verbose_name='Ссылка', blank=True)

    class Meta():
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title
