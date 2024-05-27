# Generated by Django 4.2.1 on 2024-05-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
                ('contact_information', models.TextField()),
                ('event_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('event_type', models.CharField(choices=[('Wedding', 'Wedding'), ('Birthday', 'Birthday'), ('Corporate', 'Corporate'), ('Anniversary', 'Anniversary'), ('Graduation', 'Graduation'), ('Conference', 'Conference')], max_length=20)),
                ('design_service', models.BooleanField(default=False)),
                ('number_of_guests', models.IntegerField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('downpayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Overdue', 'Overdue')], max_length=20)),
                ('event_status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=20)),
            ],
        ),
    ]