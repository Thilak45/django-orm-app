# Generated by Django 3.1.1 on 2023-07-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('referencenumber', models.CharField(help_text='reference number', max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('mobilenumber', models.IntegerField()),
            ],
        ),
    ]
