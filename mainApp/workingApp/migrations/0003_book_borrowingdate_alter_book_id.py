# Generated by Django 5.0.6 on 2024-05-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingApp', '0002_book_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowingDate',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
