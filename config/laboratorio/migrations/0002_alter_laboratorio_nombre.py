# Generated by Django 5.1.2 on 2024-12-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='nombre',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]