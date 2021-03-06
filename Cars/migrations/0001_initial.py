# Generated by Django 3.1 on 2020-08-16 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(db_index=True, max_length=20, verbose_name='Автомобиль')),
                ('reg_number', models.CharField(db_index=True, max_length=20, verbose_name='Гос.Номер')),
            ],
            options={
                'verbose_name': 'Автомобили',
                'verbose_name_plural': 'Автомобили',
                'ordering': ['-name_car'],
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_detail', models.CharField(db_index=True, max_length=20, verbose_name='Деталь')),
            ],
            options={
                'verbose_name': 'Детали',
                'verbose_name_plural': 'Детали',
                'ordering': ['-name_detail'],
            },
        ),
        migrations.CreateModel(
            name='MarkaCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(db_index=True, max_length=20, verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Марки автомобилей',
                'verbose_name_plural': 'Марки автомобилей',
                'ordering': ['-marka'],
            },
        ),
        migrations.CreateModel(
            name='RoutineMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_routine', models.CharField(db_index=True, max_length=20, verbose_name='Работа')),
            ],
            options={
                'verbose_name': 'Регламентные работы',
                'verbose_name_plural': 'Регламентные работы',
                'ordering': ['-name_routine'],
            },
        ),
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameuser', models.CharField(db_index=True, max_length=20, verbose_name='Имя')),
                ('emailuser', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-nameuser'],
            },
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FloatField(blank=True, null=True, verbose_name='Ресурс')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.cars', verbose_name='Автомобиль')),
                ('marka_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.markacars', verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'регламент работ',
                'verbose_name_plural': 'регламент работ',
            },
        ),
        migrations.CreateModel(
            name='PartsResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FloatField(blank=True, null=True, verbose_name='Ресурс')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.cars', verbose_name='Автомобиль')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.details', verbose_name='Деталь')),
            ],
            options={
                'verbose_name': 'ресурс деталей',
                'verbose_name_plural': 'ресурс деталей',
            },
        ),
        migrations.CreateModel(
            name='ModelCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(db_index=True, max_length=20, verbose_name='Модель')),
                ('marka_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.markacars', verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Модели автомобилей',
                'verbose_name_plural': 'Модели автомобилей',
                'ordering': ['-model'],
            },
        ),
        migrations.AddField(
            model_name='cars',
            name='marka_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.markacars', verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='cars',
            name='model_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.modelcars', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='cars',
            name='user_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cars.userservice', verbose_name='Автовладелец'),
        ),
    ]
