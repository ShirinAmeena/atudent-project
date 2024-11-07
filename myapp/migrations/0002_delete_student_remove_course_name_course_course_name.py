# Generated by Django 5.1.1 on 2024-10-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]