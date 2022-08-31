# Generated by Django 4.1 on 2022-08-29 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='directory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='self1', to='mysite.directory'),
        ),
        migrations.AlterField(
            model_name='file',
            name='directory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.directory'),
        ),
    ]
