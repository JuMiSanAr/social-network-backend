# Generated by Django 3.1 on 2021-03-19 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to='user_profile.UserProfile'),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='user_profile.userprofile'),
        ),
        migrations.AddField(
            model_name='post',
            name='shared_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shared_in_posts', to='post.post'),
        ),
    ]
