# Generated by Django 3.0.4 on 2020-03-12 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_code', models.CharField(max_length=4)),
                ('airport_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('coordinates', models.CharField(max_length=100)),
                ('timezone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_ref', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='airtrans.Airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport', to='airtrans.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_no', models.AutoField(primary_key=True, serialize=False)),
                ('passenger_id', models.PositiveIntegerField()),
                ('passenger_name', models.CharField(max_length=100)),
                ('contact_data', models.CharField(max_length=100)),
                ('book_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='TicketFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Flight')),
                ('ticket_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Ticket')),
            ],
            options={
                'unique_together': {('ticket_no', 'flight_id')},
            },
        ),
    ]
