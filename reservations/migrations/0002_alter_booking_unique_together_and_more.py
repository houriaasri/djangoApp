# Generated by Django 4.2.6 on 2023-10-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='reservation_slot',
            field=models.CharField(max_length=50),
        ),
    ]