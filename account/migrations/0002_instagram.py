# Generated by Django 4.2 on 2023-04-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100)),
                ('follower', models.TextField(max_length=20)),
                ('following', models.TextField(max_length=20)),
            ],
        ),
    ]