# Generated by Django 4.0.2 on 2022-02-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_board_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]