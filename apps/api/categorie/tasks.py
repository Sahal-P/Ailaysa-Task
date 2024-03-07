from celery import shared_task
from PIL import Image as PILImage, ImageFile
from django.core.files.base import ContentFile
from .models import Product
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys



@shared_task
def upload_product_picture(name, picture, image_name):
    """
    Celery task for uploading product pictures with image compression.

    This task takes a product name, picture content, and image name as input, 
    processes the image, compresses it, and uploads it to the corresponding product.

    Parameters:
        name (str): The name of the product to which the picture belongs.
        picture (bytes): The binary content of the picture.
        image_name (str): The name of the image file.

    Raises:
        FileNotFoundError: If the image file is not found.
        PILImage.DecompressionBombError: If there is an error in decompressing the image.
        Exception: For any other unexpected errors during image processing or upload.

    Returns:
        None
    """
    product = Product.objects.get(name=name)
    img = PILImage.open(ContentFile(picture))
    try:
        image_format = "jpeg"
        output = BytesIO()
        
        if img.format == "GIF":
            image_format = "gif"

        img = img.resize((400, 400), PILImage.Resampling.LANCZOS)
        img.save(output, format=image_format.upper(), quality=80)

        output.seek(0)
        image = InMemoryUploadedFile(
            output,
            "ImageField",
            f"{image_name.split('.')[0]}.{image_format}",
            f"image/{image_format}",
            sys.getsizeof(output),
            None,
        )
        product.picture.save(image.name, image)
        
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PILImage.DecompressionBombError as e:
        print(f"Image decompression error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
