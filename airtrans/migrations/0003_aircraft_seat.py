# Generated by Django 3.0.4 on 2020-04-15 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airtrans', '0002_boardingpass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('aircraft_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=10)),
                ('range', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.CharField(max_length=10)),
                ('fare_conditions', models.CharField(max_length=10)),
                ('aircraft_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Aircraft')),
            ],
            options={
                'unique_together': {('aircraft_code', 'seat_no')},
            },
        ),
    ]
