# Generated by Django 3.1.2 on 2021-09-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20210913_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion_match_performance',
            name='tierId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
