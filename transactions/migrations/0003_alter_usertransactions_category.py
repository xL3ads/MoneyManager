# Generated by Django 5.2 on 2025-05-06 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('transactions', '0002_alter_usertransactions_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransactions',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.usercategory'),
        ),
    ]
