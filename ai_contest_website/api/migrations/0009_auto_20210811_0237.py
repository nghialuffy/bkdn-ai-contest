# Generated by Django 2.2.5 on 2021-08-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210810_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='accuracy',
            field=models.FloatField(default=0.0),
        ),
    ]
