# Generated by Django 3.2.4 on 2021-08-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Form_app', '0009_delete_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='Responses',
            field=models.TextField(default=''),
        ),
    ]
