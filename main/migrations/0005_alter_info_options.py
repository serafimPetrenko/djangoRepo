# Generated by Django 4.1.3 on 2022-11-09 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_info"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="info",
            options={"ordering": ["-id"], "verbose_name": "Информация о наличии"},
        ),
    ]
