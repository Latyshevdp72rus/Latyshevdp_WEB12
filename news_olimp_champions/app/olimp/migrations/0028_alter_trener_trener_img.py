# Generated by Django 4.1 on 2022-08-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olimp', '0027_alter_trener_trener_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trener',
            name='trener_img',
            field=models.ImageField(blank=True, default='media/default.png', upload_to='media/trener/%y/%m/%d/', verbose_name='Загрузить фото'),
        ),
    ]
