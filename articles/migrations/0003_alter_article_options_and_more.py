# Generated by Django 4.2.5 on 2023-09-25 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options_alter_collection_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='descrption',
            new_name='description',
        ),
    ]
