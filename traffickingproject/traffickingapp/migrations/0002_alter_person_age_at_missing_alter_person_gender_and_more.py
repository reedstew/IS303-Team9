# Generated by Django 4.1.2 on 2022-11-22 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffickingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age_at_missing',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='race',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]
