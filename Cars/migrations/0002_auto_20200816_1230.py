# Generated by Django 3.1 on 2020-08-16 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workschedule',
            name='marka_car',
        ),
        migrations.AddField(
            model_name='workschedule',
            name='routine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Cars.routinemaintenance', verbose_name='Работа'),
        ),
        migrations.CreateModel(
            name='JournalReplacements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement_date', models.DateTimeField(db_index=True, verbose_name='Дата ремонта')),
                ('speedometer', models.FloatField(blank=True, null=True, verbose_name='Спидометр')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.cars', verbose_name='Автомобиль')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.details', verbose_name='Деталь')),
            ],
            options={
                'verbose_name': 'Журнал замен',
                'verbose_name_plural': 'Журнал замен',
                'ordering': ['-replacement_date'],
            },
        ),
    ]