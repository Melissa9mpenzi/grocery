# Generated by Django 5.0.6 on 2024-09-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery_app', '0009_produce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
