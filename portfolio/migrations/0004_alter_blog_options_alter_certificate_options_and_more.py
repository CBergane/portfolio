# Generated by Django 4.1.7 on 2023-11-29 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_portfolio_options_alter_testimonial_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blog Profiles'},
        ),
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['-date'], 'verbose_name': 'Certificate', 'verbose_name_plural': 'Certificates'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-date'], 'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolio Profiles'},
        ),
    ]