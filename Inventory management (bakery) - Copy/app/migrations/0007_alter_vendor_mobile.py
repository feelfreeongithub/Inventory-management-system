# Generated by Django 4.0.6 on 2022-08-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_unit_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='mobile',
            field=models.CharField(max_length=16),
        ),
    ]
