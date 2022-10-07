# Generated by Django 3.2.5 on 2022-07-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('gu', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=1000)),
                ('day', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=2000)),
                ('mid', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'festival',
                'managed': True,
            },
        ),
    ]