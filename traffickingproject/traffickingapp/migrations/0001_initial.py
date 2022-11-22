# Generated by Django 4.1.2 on 2022-11-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('date_missing', models.CharField(max_length=45)),
                ('age_at_missing', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=45)),
                ('race', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'people',
            },
        ),
    ]
