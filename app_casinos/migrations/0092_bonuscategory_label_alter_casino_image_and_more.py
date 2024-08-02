# Generated by Django 5.0.7 on 2024-08-02 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0091_casino_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Label Name')),
            ],
        ),
        migrations.AlterField(
            model_name='casino',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='base_casino_images/', verbose_name='Path Image'),
        ),
        migrations.AddField(
            model_name='bonus',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='bonus', to='app_casinos.bonuscategory', verbose_name='Bonus Category'),
        ),
        migrations.AddField(
            model_name='bonus',
            name='lables',
            field=models.ManyToManyField(blank=True, related_name='bonus', to='app_casinos.label', verbose_name='Labels'),
        ),
    ]