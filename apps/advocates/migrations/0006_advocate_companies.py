# Generated by Django 4.1.2 on 2022-10-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_company_advocates'),
        ('advocates', '0005_remove_advocate_companies'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='companies',
            field=models.ManyToManyField(related_name='company_id', to='companies.company'),
        ),
    ]
