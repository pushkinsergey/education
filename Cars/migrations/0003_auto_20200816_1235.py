# Generated by Django 3.1 on 2020-08-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0002_auto_20200816_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalreplacements',
            name='replacement_date',
            field=models.DateField(db_index=True, verbose_name='Дата ремонта'),
        ),
    ]
