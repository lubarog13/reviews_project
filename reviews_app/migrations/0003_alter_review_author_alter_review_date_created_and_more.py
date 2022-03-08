# Generated by Django 4.0 on 2022-03-06 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0002_alter_review_rating_alter_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews_app.user', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='review',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Логин'),
        ),
    ]