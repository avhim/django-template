# Generated by Django 4.2 on 2023-09-09 05:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0003_alter_tour_img_alter_tourdescriptionday_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tourdescriptionday",
            name="description",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
