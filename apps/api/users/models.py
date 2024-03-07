from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from constants.constant import MAX_CONTACT_NUMBER_LENGTH, USER_NAME_MAX_LENGTH
from core.common import BaseModel
from core.storage_backend import PublicMediaStorage, PrivateMediaStorage
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from decouple import config
import uuid


class CustomUserManager(BaseUserManager):
    """Custom manager for the User model."""
    def create_user(
        self, email, password=config("DEFAULT_PASSWORD", None), **extra_fields
    ):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,
        unique=True,
        db_index=True,
        verbose_name=_("Name"),
    )
    contact_number = models.CharField(
        max_length=MAX_CONTACT_NUMBER_LENGTH,
        validators=[
            RegexValidator(
                regex=r"^\d{1," + str(MAX_CONTACT_NUMBER_LENGTH) + r"}$",
                message="Contact number must contain only numeric characters.",
            )
        ],
        verbose_name=_("Contact Number"),
        null=True,
        blank=True,
    )
    email = models.EmailField(unique=True, db_index=True, verbose_name=_("Email"))
    profile_picture = models.FileField(
        upload_to="images/profile_pictures",
        storage=FileSystemStorage(),
        null=True,
        blank=True,
        verbose_name=_("Profile Picture"),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    objects = CustomUserManager()

    REQUIRED_FIELDS = ["name"]
    USERNAME_FIELD = "email"

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name
