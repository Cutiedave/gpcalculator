# Generated by Django 4.0.3 on 2022-03-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_coursegrade_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semsester',
            field=models.CharField(choices=[('1', '1'), ('2', '2')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='unit',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='coursegrade',
        ),
    ]
