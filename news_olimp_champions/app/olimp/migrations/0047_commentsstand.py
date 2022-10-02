# Generated by Django 4.1 on 2022-10-02 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('olimp', '0046_alter_commentssportsman_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsStand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Комментарии')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('moderation_is_visible', models.BooleanField(blank=True, default=False, null=True, verbose_name='Скрыть запись')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olimp.stand', verbose_name='Новость спортсмена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'КОММЕНТАРИЙ НОВОСТЕЙ',
                'verbose_name_plural': 'КОММЕНТАРИИ НОВОСТЕЙ',
            },
        ),
    ]
