from django.db import models


class Pharmacy(models.Model):
    number = models.IntegerField(verbose_name="Номер")
    location = models.TextField(null=True, blank=True, verbose_name="Адрес")
    metro_station = models.CharField(max_length=50, verbose_name="Станция метро")

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name_plural = 'Аптеки'
        verbose_name = 'Аптека'
        ordering = ['number']


class Pills(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    doze = models.FloatField(null=True, blank=True, verbose_name="Дозировка")
    amount = models.FloatField(null=True, blank=True, verbose_name="Количество")
    creator = models.CharField(max_length=50, null=True, blank=True, verbose_name="Производитель")
    receptRequired = models.BooleanField(verbose_name="Необходимость рецепта")
    category = models.ForeignKey('PillsCategory', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.FloatField(verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Лекарства'
        verbose_name = 'Лекарство'
        ordering = ['name']


class PillsCategory(models.Model):
    name = models.CharField(max_length=30, db_index=True,
                            verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории лекарств'
        verbose_name = 'Категория лекарств'
        ordering = ['name']


class Info(models.Model):
    pharmacy = models.ForeignKey('Pharmacy', null=True, on_delete=models.PROTECT, verbose_name='Аптека')
    pills = models.ForeignKey('Pills', null=True, on_delete=models.PROTECT, verbose_name='Лекарство')
    amount = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Информация о наличии'
        verbose_name_plural = 'Информация о наличии'
        ordering = ['-id']
# Create your models here.
