# Generated by Django 4.1.4 on 2022-12-11 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_alter_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dislikes',
        ),
    ]
