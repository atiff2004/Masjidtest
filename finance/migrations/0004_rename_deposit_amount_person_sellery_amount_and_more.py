# Generated by Django 5.0.6 on 2024-12-28 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_remove_person_date_person_deposit_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='deposit_amount',
            new_name='sellery_amount',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='deposit_date',
            new_name='sellery_date',
        ),
    ]
