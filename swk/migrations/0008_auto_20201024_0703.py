# Generated by Django 3.1.2 on 2020-10-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swk', '0007_merge_20201024_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracksheet',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tracksheet',
            name='num_houses_reached',
            field=models.IntegerField(default=20),
        ),
    ]
