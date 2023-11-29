# Generated by Django 4.1.7 on 2023-11-29 12:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='question',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
