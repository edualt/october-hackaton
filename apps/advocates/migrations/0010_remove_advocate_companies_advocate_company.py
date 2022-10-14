# Generated by Django 4.1.2 on 2022-10-10 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_remove_company_advocates'),
        ('advocates', '0009_advocate_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocate',
            name='companies',
        ),
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advocates', to='companies.company'),
        ),
    ]
