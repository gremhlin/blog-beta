# Generated by Django 2.2.2 on 2019-08-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateTimeField()),
                ('biography', models.TextField()),
            ],
        ),
    ]