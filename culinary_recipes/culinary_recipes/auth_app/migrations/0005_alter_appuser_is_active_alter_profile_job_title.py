# Generated by Django 4.1.3 on 2022-12-26 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_delete_customgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job_title',
            field=models.CharField(choices=[('waiter', 'Сервитьор'), ('cook', 'Готвач'), ('manager', 'Мениджър')], max_length=7, verbose_name='Choice you job title'),
        ),
    ]
