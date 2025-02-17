# Generated by Django 3.1.1 on 2022-12-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EMP_ID', models.CharField(help_text='Phonenumber', max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Post', models.CharField(max_length=30)),
                ('Salary', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
