# Generated by Django 3.2.25 on 2024-05-12 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_book_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='session_id',
        ),
        migrations.AddField(
            model_name='book',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]