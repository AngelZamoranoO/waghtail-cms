# Generated by Django 5.0.3 on 2024-03-12 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StandartPage',
            new_name='StandardPage',
        ),
    ]