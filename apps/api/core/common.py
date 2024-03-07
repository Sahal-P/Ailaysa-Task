from django.db import models
import uuid


class BaseModel(models.Model):
    """
    Abstract base model for all database models.

    This base model defines a common set of fields and behaviors to be inherited
    by all database models in the application. It uses a UUID as the primary key
    for better consistency and security.

    Attributes:
        id (UUIDField): The primary key field containing a unique identifier for each instance.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )

    class Meta:
        abstract = True