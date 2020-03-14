from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Файл')
    name = models.CharField('Подпись', max_length=100)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('auth.User', related_name='users_file', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Файл")