# Generated by Django 3.0.4 on 2020-03-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0002_auto_20200321_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
