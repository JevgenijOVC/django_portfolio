# Generated by Django 4.2.6 on 2023-11-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jevgenij', '0002_rename_greatings_1_home_greetings_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=50),
        ),
    ]
