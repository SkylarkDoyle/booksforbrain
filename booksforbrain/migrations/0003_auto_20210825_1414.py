# Generated by Django 3.2.5 on 2021-08-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksforbrain', '0002_remove_ownedbook_owned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownedbook',
            name='book_sold',
        ),
        migrations.AddField(
            model_name='ownedbook',
            name='owned',
            field=models.CharField(choices=[('not owned', 'not owned'), ('owned', 'owned')], default='not owned', max_length=100, null=True),
        ),
    ]
