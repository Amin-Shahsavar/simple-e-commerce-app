# Generated by Django 4.2.5 on 2023-10-07 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_options_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='articles.collection', verbose_name='Collection'),
        ),
    ]
