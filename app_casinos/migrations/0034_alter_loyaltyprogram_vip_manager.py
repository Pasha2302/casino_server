# Generated by Django 5.0 on 2024-01-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0033_rename_loyalty_program_cashback_level_loyalty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyaltyprogram',
            name='vip_manager',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default=None, max_length=3, null=True),
        ),
    ]