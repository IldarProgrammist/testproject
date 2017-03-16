from django.db import models


class Person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return "Пользователь %s" % (self.name)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = 'Пользователи'
