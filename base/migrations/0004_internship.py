# Generated by Django 4.2.4 on 2023-08-15 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_certification_certification_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('issuing_organization', models.CharField(max_length=200)),
                ('date_completed', models.DateField(default=django.utils.timezone.now)),
                ('certification_link', models.URLField(default='www.google.com')),
            ],
        ),
    ]
