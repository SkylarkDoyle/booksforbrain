# Generated by Django 3.2.5 on 2021-08-26 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booksforbrain', '0012_alter_ownedbook_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownedbook',
            name='reader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned', to=settings.AUTH_USER_MODEL),
        ),
    ]
