# Generated by Django 3.1.2 on 2020-10-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
