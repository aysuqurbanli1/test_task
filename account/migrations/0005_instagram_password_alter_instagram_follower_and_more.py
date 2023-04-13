# Generated by Django 4.2 on 2023-04-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_instagram_follower_alter_instagram_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='follower',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='following',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
