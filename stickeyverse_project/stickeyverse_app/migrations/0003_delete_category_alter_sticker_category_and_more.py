# Generated by Django 4.2.2 on 2023-07-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickeyverse_app', '0002_rename_name_sticker_stickername_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='sticker',
            name='category',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='sticker',
            name='stickername',
            field=models.CharField(max_length=150),
        ),
    ]