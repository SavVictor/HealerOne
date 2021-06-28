# Generated by Django 3.1.7 on 2021-05-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serena', '0002_auto_20210509_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='description',
            new_name='short_description',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='link',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='long_description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]