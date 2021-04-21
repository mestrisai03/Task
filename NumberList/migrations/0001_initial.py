# Generated by Django 3.2 on 2021-04-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('Nid', models.IntegerField(primary_key=True, serialize=False)),
                ('numbers', models.IntegerField(max_length=100)),
            ],
            options={
                'db_table': 'Numbers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('Wid', models.IntegerField(primary_key=True, serialize=False)),
                ('words', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Words',
                'managed': True,
            },
        ),
    ]
