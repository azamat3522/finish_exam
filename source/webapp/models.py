from django.db import models


TYPE_CHOICES = (
    ('common', 'Общий'),
    ('hidden', 'Скрытый'),
    ('private', 'Приватный'),
)


class File(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Файл')
    name = models.CharField('Подпись', max_length=100)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('auth.User', related_name='users_file', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Автор')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0],
                            verbose_name='Тип')
    private_group = models.ManyToManyField('auth.User', related_name='file_private', verbose_name='Группа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Файл")
        verbose_name_plural = ("Файлы")