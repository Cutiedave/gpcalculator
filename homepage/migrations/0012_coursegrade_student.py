# Generated by Django 4.0.3 on 2022-03-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_remove_coursegrade_student_coursegrade_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegrade',
            name='student',
            field=models.ManyToManyField(null=True, to='homepage.student'),
        ),
    ]
