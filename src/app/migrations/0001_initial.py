# Generated by Django 2.2.6 on 2019-10-04 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Permissions',
                'db_table': 'permissions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Permission')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
        ),
    ]
