# Generated by Django 4.1.2 on 2022-10-11 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0015_rename_company_advocate_compani'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocate',
            old_name='compani',
            new_name='company',
        ),
    ]
