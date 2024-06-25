from django.db import models

class Info(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        null=False,
        blank=False,
    )
    credit = models.IntegerField(
        verbose_name='Кредит',
        default=0
    )
    percent = models.IntegerField(
        verbose_name='Процентная ставка',
        choices=[
            (16, '16%'),
            (18, '18%'),
            (22, '22%'),
            (24, '24%'),
        ],
        default=24
    )
    duration = models.IntegerField(
        verbose_name='Срок погашения',
        default=12
    )
    def __str__(self) -> str:
        return self.name
