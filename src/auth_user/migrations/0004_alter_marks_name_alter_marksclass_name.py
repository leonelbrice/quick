# Generated by Django 4.0.3 on 2022-06-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_faculte_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('test 1', 'test 1'), ('test 2', 'test 2'), ('test 3', 'test 3'), ('Controle continu', 'Controle continu'), ('Travaux pratique', 'Travaux pratique'), ('Session normale', 'Session normale')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('test 1', 'test 1'), ('test 2', 'test 2'), ('test 3', 'test 3'), ('Controle continu', 'Controle continu'), ('Travaux pratique', 'Travaux pratique'), ('Session normale', 'Session normale')], default='test 1', max_length=50),
        ),
    ]
