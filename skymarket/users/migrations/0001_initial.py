# Generated by Django 3.2.6 on 2024-01-25 19:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя пользователя')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия пользователя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='телефон для связи')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='электронная почта пользователя ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/avatars', verbose_name='аватарка пользователя')),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=50, verbose_name='Роль')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
