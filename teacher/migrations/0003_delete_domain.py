# Generated by Django 2.2.12 on 2020-06-10 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_domain_updated_domain'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Domain',
        ),
    ]