# Generated by Django 4.0.3 on 2022-10-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreport',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, help_text='Timestamp of this snapshot'),
        ),
    ]
