# Generated by Django 4.0.3 on 2022-03-18 20:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0010_alter_coursegrade_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursegrade',
            name='student',
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]