# Generated by Django 4.2 on 2023-04-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_instagram_password_alter_instagram_follower_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagram',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
