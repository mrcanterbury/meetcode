# Generated by Django 4.0.2 on 2022-02-04 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_board_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
