# Generated by Django 4.1.2 on 2024-01-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='car_images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(null=True),
        ),
    ]