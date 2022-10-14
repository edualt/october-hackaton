# Generated by Django 4.1.2 on 2022-10-11 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_alter_company_href'),
        ('advocates', '0012_alter_advocate_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advocates', to='companies.company'),
        ),
    ]
