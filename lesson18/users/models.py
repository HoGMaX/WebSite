from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField('Аватар',default='user_default_icon.png',upload_to = 'default_icon')

    Gender = [
        ('m','мужской'),
        ('w','женский'),
        ('o','нет'),
    ]
    gender = models.CharField('Пол:',max_length=2,default='o',choices=Gender)
    agreement = models.BooleanField(default = False)
    def __str__(self):
        return f'Профайл пользователя {self.user.username}'
    def save(self, *args,**kwargs):
        super().save()

        img = Image.open(self.user_img.path)

        if img.height > 256 or img.width > 256:
            img.thumbnail(resize)
            img.save(self.user_img.path)

    class Meta():
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
