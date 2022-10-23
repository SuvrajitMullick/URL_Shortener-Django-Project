# Generated by Django 4.1.2 on 2022-10-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URL_Shortener', '0002_countrydata_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('country_count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Country Data',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=50)),
                ('device_count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Device Data',
            },
        ),
        migrations.DeleteModel(
            name='CountryData',
        ),
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name_plural': 'Details'},
        ),
        migrations.AlterModelOptions(
            name='url_table',
            options={'verbose_name_plural': 'URL Tables'},
        ),
    ]
