# Generated by Django 2.1.2 on 2018-10-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikaldeiraapp', '0003_auto_20181001_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lore',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='lore',
            name='image',
            field=models.ImageField(null='False', upload_to='media'),
        ),
    ]
