# Generated by Django 4.0.6 on 2022-08-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_total_bal_inventory_total_bal_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='total_bal_qty',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total_amt',
            field=models.FloatField(editable=False),
        ),
    ]