# Generated by Django 4.0.3 on 2022-06-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0002_faculte_dept_faculte'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculte',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo'),
        ),
    ]
