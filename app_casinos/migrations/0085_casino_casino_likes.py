# Generated by Django 5.0.7 on 2024-08-01 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0084_bonus_special_promo_category_bonus_special_side_bar'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='casino_likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
