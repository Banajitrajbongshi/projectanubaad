# Generated by Django 3.1.4 on 2021-04-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions_base',
            name='correct',
            field=models.CharField(default='', max_length=1),
        ),
    ]