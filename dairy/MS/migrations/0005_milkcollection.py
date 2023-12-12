# Generated by Django 4.2.3 on 2023-12-04 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0004_feedmonitoring'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.CharField(max_length=20, unique=True)),
                ('date', models.DateField()),
                ('liter', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_per_liter', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cow_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MS.cowinfo')),
            ],
        ),
    ]
