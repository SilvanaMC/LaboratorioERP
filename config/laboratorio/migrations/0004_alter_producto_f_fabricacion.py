# Generated by Django 4.1.1 on 2024-12-18 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_alter_producto_f_fabricacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(),
        ),
    ]
