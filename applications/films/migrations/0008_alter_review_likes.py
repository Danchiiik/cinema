# Generated by Django 4.1.4 on 2022-12-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_alter_review_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]