# Generated by Django 5.0.6 on 2024-12-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_rename_deposit_amount_person_sellery_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='name',
            field=models.CharField(max_length=500, verbose_name='فنڈ کا نام'),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='expense_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='اخراجات کا نام'),
        ),
    ]
