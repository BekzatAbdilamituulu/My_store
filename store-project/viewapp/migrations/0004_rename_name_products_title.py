# Generated by Django 4.1.7 on 2023-03-25 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewapp', '0003_rename_title_products_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='title',
        ),
    ]