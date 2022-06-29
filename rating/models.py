from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from main.models import Massage


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField(default=0)


    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]

    def __str__(self):
        return f'{self.value}'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    massage = models.ForeignKey(Massage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.massage}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
