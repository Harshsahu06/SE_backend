# Generated by Django 5.0.3 on 2024-05-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0002_rename_name_hospital_namee"),
    ]

    operations = [
        migrations.AddField(
            model_name="hospital",
            name="image",
            field=models.ImageField(default=111, upload_to="img"),
            preserve_default=False,
        ),
    ]
