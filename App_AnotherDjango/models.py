from django.db import models
from django.contrib import  admin
from django.utils import timezone
from django.utils.html import format_html


# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    text = models.TextField('текст')
    price = models.FloatField('цена')
    user = models.CharField('пользователь', max_length=126)  # Пользователь (пока-что просто имя)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField("торг", help_text='Возможен торг или нет', default=False)

    def __str__(self) -> str:
        return f'Advertisements(id = {self.id}, title = {self.title}, price = {self.price})'

    class Meta:
        db_table = 'advertisements'

    @admin.display(description="дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green; font-weight = bold;">Сегодня в {}</span>', create_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description="дата обновления")
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            create_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:grey; font-weight = bold;">Сегодня в {}</span>', create_time
            )
        return self.update_at.strftime('%d.%m.%Y at %H:%M:%S')