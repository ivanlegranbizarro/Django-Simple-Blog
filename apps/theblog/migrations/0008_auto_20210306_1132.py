# Generated by Django 3.1.7 on 2021-03-06 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_auto_20210306_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='theblog.category', verbose_name='Categoría'),
        ),
    ]
