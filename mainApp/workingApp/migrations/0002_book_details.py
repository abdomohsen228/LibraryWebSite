# Generated by Django 5.0.6 on 2024-05-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]