# Generated by Django 4.0.2 on 2022-02-06 05:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_category_board_author_message_board_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='board',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]