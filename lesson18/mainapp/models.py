from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Cource(models.Model):
    slug = models.SlugField('Имя курса',max_length =100,unique=True)
    titel = models.CharField('Заголовок курса',max_length=100)
    description = models.TextField('Описание курса')
    img = models.ImageField(default='default.png',upload_to='cource_img')
    name = models.ForeignKey(User,verbose_name='Имя', on_delete = models.CASCADE)

    def get_absolute_url(self):
        return redirect('add_cource')
    def __str__(self):
        return f'Курс: {self.titel}'

    class Meta():
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'