# Generated by Django 5.0.3 on 2024-03-06 16:28

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categorie", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="profile_picture",
            field=models.FileField(
                blank=True,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="images/product/",
                verbose_name="Product Picture",
            ),
        ),
    ]
