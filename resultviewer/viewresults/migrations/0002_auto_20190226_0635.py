# Generated by Django 2.1.7 on 2019-02-26 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewresults', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='id',
        ),
        migrations.RemoveField(
            model_name='result',
            name='id',
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='result',
            name='reg_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
