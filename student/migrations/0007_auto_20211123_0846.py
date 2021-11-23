# Generated by Django 3.2.4 on 2021-11-23 08:46

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20211123_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybookedslots',
            name='date',
            field=models.DateField(default=None, null=True, validators=[student.models.myBookedSlots.validate_date]),
        ),
        migrations.AlterField(
            model_name='mybookedslots',
            name='time',
            field=models.TimeField(default=None, null=True),
        ),
    ]
