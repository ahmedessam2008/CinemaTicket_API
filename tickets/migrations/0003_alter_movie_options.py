# Generated by Django 4.0.6 on 2022-08-03 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_userdata_options_userdata_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-date']},
        ),
    ]
