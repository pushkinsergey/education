# Generated by Django 3.1 on 2021-02-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0016_auto_20210226_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='planned_date',
            field=models.DateField(db_index=True, null=True, verbose_name='Планируемая дата замены'),
        ),
    ]
