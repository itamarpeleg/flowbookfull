# Generated by Django 3.2.12 on 2022-03-17 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_choice_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='name_of_flower',
        ),
    ]
