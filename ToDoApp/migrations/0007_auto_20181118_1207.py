# Generated by Django 2.1.3 on 2018-11-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0006_auto_20181118_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]