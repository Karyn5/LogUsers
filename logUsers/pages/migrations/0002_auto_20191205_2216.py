# Generated by Django 2.1.7 on 2019-12-06 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personlog',
            name='personId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='pages.Person'),
        ),
    ]
