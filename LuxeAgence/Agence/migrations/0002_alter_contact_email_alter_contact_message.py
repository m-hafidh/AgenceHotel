# Generated by Django 4.2.4 on 2024-05-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
