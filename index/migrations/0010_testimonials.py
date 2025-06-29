# Generated by Django 5.2 on 2025-06-26 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='Testimonial')),
                ('text', models.TextField()),
            ],
        ),
    ]
