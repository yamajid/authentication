# Generated by Django 5.1.5 on 2025-02-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
