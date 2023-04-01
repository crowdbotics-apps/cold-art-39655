# Generated by Django 2.2.28 on 2023-04-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
