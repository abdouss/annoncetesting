# Generated by Django 2.1.1 on 2018-09-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appannonce', '0002_annonce_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='lieuaproximité',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='galerie',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', verbose_name='profile annonce ', width_field='width_field'),
        ),
    ]
