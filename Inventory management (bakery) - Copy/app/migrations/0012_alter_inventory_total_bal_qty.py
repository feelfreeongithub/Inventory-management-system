# Generated by Django 4.0.6 on 2022-08-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_inventory_total_bal_qty_alter_sale_total_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='total_bal_qty',
            field=models.FloatField(editable=False, null=True),
        ),
    ]
