# Generated by Django 4.1.4 on 2022-12-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_remove_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveIntegerField(choices=[(1, '1 - Too bad'), (2, '2 - Bad'), (3, '3 - Normal'), (4, '4 - Good'), (5, '5 - Perfect')]),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
