# Generated by Django 3.1 on 2020-08-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20200814_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
