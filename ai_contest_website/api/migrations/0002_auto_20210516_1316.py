# Generated by Django 2.2.5 on 2021-05-16 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='created_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_created_user', to='api.User'),
        ),
    ]
