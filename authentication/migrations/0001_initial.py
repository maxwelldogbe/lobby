# Generated by Django 5.0.4 on 2024-05-01 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telephone', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=10)),
                ('category', models.CharField(choices=[('investor', 'Investor'), ('personnel', 'Personnel')], max_length=20)),
            ],
        ),
    ]