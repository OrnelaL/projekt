# Generated by Django 5.2.3 on 2025-06-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_surname', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_comment', models.TextField(blank=True, max_length=2000, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
