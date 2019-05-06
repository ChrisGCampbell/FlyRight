# Generated by Django 2.1.1 on 2018-10-20 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icarus_backend', '0007_auto_20181018_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='airboss',
            new_name='airbosses',
        ),
        migrations.AddField(
            model_name='department',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]