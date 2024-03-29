# Generated by Django 5.0.3 on 2024-03-06 15:41

import django.core.files.storage
import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, unique=True, verbose_name="Name"
                    ),
                ),
                (
                    "contact_number",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Contact number must contain only numeric characters.",
                                regex="^\\d{1,15}$",
                            )
                        ],
                        verbose_name="Contact Number",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "profile_picture",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=django.core.files.storage.FileSystemStorage(),
                        upload_to="images/profile_pictures",
                        verbose_name="Profile Picture",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Users",
                "ordering": ["name"],
            },
        ),
    ]
