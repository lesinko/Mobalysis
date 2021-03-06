# Generated by Django 3.1.2 on 2021-11-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0064_runepath_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleStats',
            fields=[
                ('role', models.TextField(blank=True, null=True)),
                ('championid', models.TextField(blank=True, db_column='championId', null=True)),
                ('region', models.TextField(blank=True, null=True)),
                ('tier', models.TextField(blank=True, null=True)),
                ('fgm', models.TextField(blank=True, null=True)),
                ('winrate', models.FloatField(blank=True, null=True)),
                ('pickrate', models.FloatField(blank=True, null=True)),
                ('games_played', models.BigIntegerField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'role_stats',
                'managed': False,
            },
        ),
    ]
