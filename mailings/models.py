from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^7\d{10}$', message="Номер телефона необходимо вводить в формате: '7XXXXXXXXX'. разрешено только 11 цифр. (X - цифра от 0 до 9)")
    number = models.CharField(validators=[phone_regex], max_length=11, unique=True, blank=False)
    code = models.CharField(max_length=10)
    tag = models.CharField(null=True, blank=False, max_length=50)
    time_zone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Mailing(models.Model):
    start_send_time = models.DateTimeField()
    text = models.TextField()
    tag = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    end_send_time = models.DateTimeField()

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class Message(models.Model):
    STATUS_CHOICES = (
        ('S', 'send'),
        ('N', 'not send'),
    )
    send_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    def __str__(self):
        return f'{self.mailing} {self.contact} {self.status}'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
