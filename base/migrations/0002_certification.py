# Generated by Django 4.2.4 on 2023-08-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('issuing_organization', models.CharField(max_length=200)),
                ('date_completed', models.DateField()),
            ],
        ),
    ]
