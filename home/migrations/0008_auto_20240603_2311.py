# Generated by Django 3.2.25 on 2024-06-03 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_auto_20240525_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='rentbook',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='rentbook',
            name='book_name',
        ),
        migrations.RemoveField(
            model_name='rentbook',
            name='student_name',
        ),
        migrations.AddField(
            model_name='book',
            name='barcode',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='copies',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rentbook',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rentbook',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='student',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rentbook',
            name='student',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.student'),
            preserve_default=False,
        ),
    ]