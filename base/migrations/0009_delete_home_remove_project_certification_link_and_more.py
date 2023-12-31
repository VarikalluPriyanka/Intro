# Generated by Django 4.2.4 on 2023-08-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_delete_portfolio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.RemoveField(
            model_name='project',
            name='certification_link',
        ),
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.URLField(default='www.github.com'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]