# Generated by Django 4.1.4 on 2022-12-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_alter_films_options_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
