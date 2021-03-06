# Generated by Django 3.2.9 on 2021-11-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
    ]
