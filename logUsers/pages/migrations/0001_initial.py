# Generated by Django 2.1.7 on 2019-12-06 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeIn', models.DateTimeField(auto_now=True)),
                ('timeOut', models.DateTimeField(blank=True, null=True)),
                ('personId', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pages.Person')),
            ],
        ),
    ]