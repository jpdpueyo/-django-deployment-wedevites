# Generated by Django 2.1 on 2018-08-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(default='', max_length=128)),
                ('status', models.CharField(choices=[('G', 'Going'), ('N', 'Not going')], default='Unspecified', max_length=1, null=True)),
            ],
        ),
    ]
