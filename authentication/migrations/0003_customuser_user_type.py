# Generated by Django 4.2.10 on 2024-02-27 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_profile_full_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                blank=True,
                choices=[("student", "Student"), ("university", "University")],
                max_length=10,
                null=True,
            ),
        ),
    ]
