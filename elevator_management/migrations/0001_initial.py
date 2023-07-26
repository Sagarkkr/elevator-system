# Generated by Django 4.2.3 on 2023-07-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_operational', models.BooleanField(default=True)),
                ('current_floor', models.IntegerField()),
                ('destination_floor', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('moving', 'Moving'), ('stopped', 'Stopped'), ('idle', 'Idle'), ('maintenance', 'Maintenance')], default='moving', max_length=50)),
                ('direction', models.CharField(choices=[('up', 'Up'), ('down', 'Down'), ('stop', 'Stop')], default='up', max_length=50)),
                ('max_occupancy', models.IntegerField()),
                ('current_occupancy', models.IntegerField()),
                ('min_floor', models.IntegerField()),
                ('max_floor', models.IntegerField()),
            ],
        ),
    ]
