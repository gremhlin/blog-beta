# Generated by Django 2.2.2 on 2019-08-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('Academic', 'Academic Piece'), ('Article', 'Article'), ('Web', 'Web Project'), ('Life', 'Life Update')], max_length=15),
        ),
    ]
