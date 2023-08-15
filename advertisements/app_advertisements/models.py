from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время изменения', auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_at

    @admin.display(description='Дата редактирования')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;"> Сегодня в {} </span>', updated_time
            )
        return self.updated_at

    def __str__(self):
        return f"Advertisement(id={self.pk}, title={self.title}, price={self.price:.2f})"

    class Meta:
        db_table = 'advertisements'
