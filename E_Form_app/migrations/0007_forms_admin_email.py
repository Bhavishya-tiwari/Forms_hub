# Generated by Django 3.2.4 on 2021-08-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Form_app', '0006_auto_20210827_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='Admin_Email',
            field=models.CharField(default=3, max_length=550),
            preserve_default=False,
        ),
    ]
