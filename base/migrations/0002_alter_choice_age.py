# Generated by Django 3.2.12 on 2022-03-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='age',
            field=models.IntegerField(),
        ),
    ]