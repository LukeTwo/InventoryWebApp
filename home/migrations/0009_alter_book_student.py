# Generated by Django 3.2.25 on 2024-06-03 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20240603_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student'),
        ),
    ]
