from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Storage class for static files served from Amazon S3.

    This storage class is used for managing static files (e.g., CSS, JavaScript)
    served from Amazon S3. It sets the location to 'static' and the default ACL
    to 'public-read' to allow public access to static files.

    Attributes:
        location (str): The location path within the S3 bucket where static files are stored.
        default_acl (str): The default Access Control List (ACL) for static files (public-read).
    """
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    """
    Storage class for public media files served from Amazon S3.

    This storage class is used for managing public media files served from Amazon S3.
    It sets the location to 'media', the default ACL to 'public-read', and disables
    file overwriting to prevent accidental data loss.

    Attributes:
        location (str): The location path within the S3 bucket where public media files are stored.
        default_acl (str): The default Access Control List (ACL) for public media files (public-read).
        file_overwrite (bool): Flag indicating whether file overwriting is allowed (False).
    """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    
class PrivateMediaStorage(S3Boto3Storage):
    """
    Storage class for private media files served from Amazon S3.

    This storage class is used for managing private media files served from Amazon S3.
    It sets the location to 'private', the default ACL to 'private', and disables
    file overwriting and custom domain to ensure private access and prevent data loss.

    Attributes:
        location (str): The location path within the S3 bucket where private media files are stored.
        default_acl (str): The default Access Control List (ACL) for private media files (private).
        file_overwrite (bool): Flag indicating whether file overwriting is allowed (False).
        custom_domain (bool): Flag indicating whether to use a custom domain (False).
    """
    location = 'private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False