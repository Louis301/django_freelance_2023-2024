# Generated by Django 5.0 on 2024-01-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_canvasmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvasmodel',
            name='pen_color',
            field=models.CharField(default='black', max_length=10),
        ),
        migrations.AlterField(
            model_name='canvasmodel',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
