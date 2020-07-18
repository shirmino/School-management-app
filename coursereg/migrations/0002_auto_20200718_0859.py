# Generated by Django 3.0.5 on 2020-07-18 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursereg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='code',
        ),
        migrations.RemoveField(
            model_name='coursemodel',
            name='fees',
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='email',
            field=models.EmailField(default='User + "@gmail.com"', max_length=30),
        ),
    ]
