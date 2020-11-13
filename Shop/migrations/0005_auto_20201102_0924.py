# Generated by Django 3.0.3 on 2020-11-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('1', 'fruct'), ('2', 'veg'), (None, 'Unknown')], max_length=20, null=True),
        ),
    ]
