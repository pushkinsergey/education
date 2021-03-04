# Generated by Django 3.1 on 2021-02-23 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cars', '0008_auto_20210212_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='car',
        ),
        migrations.RemoveField(
            model_name='modelcars',
            name='marka_car',
        ),
        migrations.RemoveField(
            model_name='partsresource',
            name='car',
        ),
        migrations.RemoveField(
            model_name='partsresource',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='replacments',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='replacments',
            name='event',
        ),
        migrations.RemoveField(
            model_name='work',
            name='event',
        ),
        migrations.RemoveField(
            model_name='work',
            name='routine',
        ),
        migrations.RemoveField(
            model_name='workschedule',
            name='car',
        ),
        migrations.RemoveField(
            model_name='workschedule',
            name='routine',
        ),
        migrations.AlterField(
            model_name='userservice',
            name='system_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
        migrations.DeleteModel(
            name='Details',
        ),
        migrations.DeleteModel(
            name='Journal',
        ),
        migrations.DeleteModel(
            name='MarkaCars',
        ),
        migrations.DeleteModel(
            name='ModelCars',
        ),
        migrations.DeleteModel(
            name='PartsResource',
        ),
        migrations.DeleteModel(
            name='Replacments',
        ),
        migrations.DeleteModel(
            name='RoutineMaintenance',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
        migrations.DeleteModel(
            name='WorkSchedule',
        ),
    ]
