# Generated by Django 4.2.14 on 2024-07-28 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_exerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
