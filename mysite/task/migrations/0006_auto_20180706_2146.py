# Generated by Django 2.0.7 on 2018-07-06 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20180705_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='usertask',
            name='user',
        ),
        migrations.AddField(
            model_name='usertotask',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.UserTask'),
        ),
    ]