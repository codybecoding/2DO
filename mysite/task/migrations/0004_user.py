# Generated by Django 2.0.6 on 2018-07-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20180628_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
