# Generated by Django 3.1.7 on 2021-03-07 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_auto_20210307_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theblog.category'),
        ),
    ]