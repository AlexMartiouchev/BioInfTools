# Generated by Django 4.0.2 on 2022-02-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricheck', '0005_delete_resultfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcf', models.FileField(upload_to='files')),
                ('bed', models.FileField(upload_to='files')),
            ],
        ),
    ]
