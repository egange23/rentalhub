# Generated by Django 4.2.2 on 2023-07-01 00:34

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_customuserverification_email_code_entered_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuserverification",
            old_name="email_code_matched",
            new_name="email_verified",
        ),
        migrations.AlterField(
            model_name="customuserverification",
            name="email_code_sent",
            field=models.CharField(
                default=accounts.models.generateOTP, max_length=6, null=True
            ),
        ),
    ]
