# Generated by Django 4.1.2 on 2022-10-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=500)),
                ('custom_name', models.CharField(max_length=50, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('visit_count', models.IntegerField(default=0)),
            ],
        ),
    ]
