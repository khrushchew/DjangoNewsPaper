# Generated by Django 5.0.4 on 2024-04-25 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='rating_of_post',
            new_name='rating',
        ),
    ]
