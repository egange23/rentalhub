# Generated by Django 4.2.2 on 2023-07-01 09:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0007_rename_email_code_matched_customuserverification_email_verified_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUserVerification",
        ),
    ]
