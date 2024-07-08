# Generated by Django 3.2.25 on 2024-07-08 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20240605_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copies',
        ),
        migrations.AlterField(
            model_name='rentbook',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.book'),
        )
    ]
