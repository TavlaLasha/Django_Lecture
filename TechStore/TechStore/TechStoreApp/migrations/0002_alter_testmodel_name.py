# Generated by Django 4.0 on 2022-11-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechStoreApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.TextField(null=True),
        ),
    ]