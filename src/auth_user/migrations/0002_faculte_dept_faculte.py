# Generated by Django 4.0.3 on 2022-06-27 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculte',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('uo', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='dept',
            name='faculte',
            field=models.ForeignKey(default='FACSCIENCES', on_delete=django.db.models.deletion.CASCADE, to='auth_user.faculte'),
        ),
    ]
