# Generated by Django 5.0.6 on 2024-09-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery_app', '0010_alter_produce_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockx',
            name='issued_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
