# Generated by Django 3.2.4 on 2021-08-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Form_app', '0005_rename_extra_info_forms_disc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forms',
            old_name='Timestamp_End',
            new_name='cd',
        ),
        migrations.RenameField(
            model_name='forms',
            old_name='Timestamp_Sheduled',
            new_name='sd',
        ),
        migrations.AddField(
            model_name='forms',
            name='ct',
            field=models.CharField(default=33, max_length=550),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forms',
            name='st',
            field=models.CharField(default=88, max_length=505),
            preserve_default=False,
        ),
    ]
