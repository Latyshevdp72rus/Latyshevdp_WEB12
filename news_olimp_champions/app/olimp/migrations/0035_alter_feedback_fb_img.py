# Generated by Django 4.1 on 2022-09-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olimp', '0034_alter_feedback_fb_img_alter_feedback_fb_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='fb_img',
            field=models.ImageField(null=True, upload_to='media/feedback/%y/%m/%d/', verbose_name='Загрузить фото'),
        ),
    ]