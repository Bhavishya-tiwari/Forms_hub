# Generated by Django 3.2.4 on 2021-08-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Form_app', '0007_forms_admin_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.CharField(max_length=700)),
                ('ResponseJson', models.TextField(default='')),
                ('Extras', models.TextField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='forms',
            name='ResponseJson',
        ),
    ]
