# Generated by Django 3.2.25 on 2024-06-05 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_book_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='book_name',
        ),
    ]
