# Generated by Django 3.2.15 on 2022-09-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=36, unique=True),
        ),
    ]
