# Generated by Django 4.0.4 on 2022-04-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='chek',
            field=models.BooleanField(default=False),
        ),
    ]
