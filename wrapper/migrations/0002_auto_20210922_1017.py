# Generated by Django 3.2.7 on 2021-09-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrapper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Job_Title', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('Unit', models.CharField(max_length=200, null=True)),
                ('Status', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Employees',
            new_name='Profile',
        ),
    ]
