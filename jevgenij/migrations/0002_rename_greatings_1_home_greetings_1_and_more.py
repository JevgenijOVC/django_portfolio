# Generated by Django 4.2.6 on 2023-10-31 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jevgenij', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='greatings_1',
            new_name='greetings_1',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='greatings_2',
            new_name='greetings_2',
        ),
    ]
