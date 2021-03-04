# Generated by Django 3.1 on 2021-02-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0019_resources_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'ordering': ['name_detail'], 'verbose_name': 'Деталь/Работа', 'verbose_name_plural': 'Деталь/Работа'},
        ),
        migrations.AlterField(
            model_name='resources',
            name='last_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата ремонта'),
        ),
        migrations.AlterField(
            model_name='resources',
            name='planned_date',
            field=models.DateField(blank=True, null=True, verbose_name='Планируемая дата замены'),
        ),
    ]
