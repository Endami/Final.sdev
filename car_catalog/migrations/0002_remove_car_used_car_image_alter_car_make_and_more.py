# Generated by Django 5.0.6 on 2024-05-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='used',
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='new',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
