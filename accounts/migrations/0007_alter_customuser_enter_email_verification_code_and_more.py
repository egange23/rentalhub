# Generated by Django 4.2.3 on 2023-07-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_enter_email_verification_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='enter_email_verification_code',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_verification_code',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]
