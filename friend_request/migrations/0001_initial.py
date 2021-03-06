# Generated by Django 3.1 on 2021-03-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Accepted'), ('R', 'Rejected'), ('P', 'Pending')], default='P', max_length=1)),
                ('resolved_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
