# Generated by Django 3.1.1 on 2020-10-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orka', '0004_auto_20201009_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
