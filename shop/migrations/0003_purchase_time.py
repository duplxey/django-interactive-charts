# Generated by Django 3.1.6 on 2021-02-04 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_purchase_successful'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]