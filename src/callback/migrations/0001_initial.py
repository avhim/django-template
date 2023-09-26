# Generated by Django 4.2 on 2023-09-25 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CallBack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=40)),
                ("phone_number", models.CharField(default="", max_length=15)),
                ("url", models.URLField(default="")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]