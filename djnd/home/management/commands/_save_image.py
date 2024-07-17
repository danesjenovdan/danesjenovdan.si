import os
import traceback

import requests
from django.core.files.base import ContentFile
from django.core.management.base import CommandError
from wagtail.images.models import Image


def get_image(command, url, tag):
    if not url:
        return None

    if url == "https://danesjenovdan.si/img/djndog.png":
        return None

    path, filename = os.path.split(url)
    filename = f"{tag}-{filename}"

    try:
        image = Image.objects.get(title=filename)
        return image
    except Image.DoesNotExist:
        pass

    return None


def save_image(command, url, tag):
    if not url:
        return None

    if url == "https://danesjenovdan.si/img/djndog.png":
        return None

    path, filename = os.path.split(url)
    filename = f"{tag}-{filename}"

    try:
        image = Image.objects.get(title=filename)
        return image
    except Image.DoesNotExist:
        pass

    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image(title=filename)
        image.file.save(filename, ContentFile(response.content))
        image.tags.add(tag)
        image.tags.add("imported")
        image.save()
        return image
    except requests.RequestException as e:
        command.stdout.write("")
        raise CommandError(f"Failed to fetch image: {e}")
    except Exception as e:
        command.stdout.write("")
        traceback.print_exc()
        raise CommandError(f"Failed to save image: {e}")
