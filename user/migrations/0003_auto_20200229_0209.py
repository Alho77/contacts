# Generated by Django 3.0.3 on 2020-02-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200229_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='confirmed'),
        ),
        migrations.AddField(
            model_name='phone',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='confirmed'),
        ),
    ]