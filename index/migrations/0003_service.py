# Generated by Django 5.2 on 2025-06-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_about_contactlist_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
