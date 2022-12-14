# Generated by Django 4.1.3 on 2022-11-09 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_pills_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="info",
            name="pharmacy",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main.pharmacy",
                verbose_name="Аптека",
            ),
        ),
        migrations.AddField(
            model_name="info",
            name="pills",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main.pills",
                verbose_name="Лекарство",
            ),
        ),
    ]
