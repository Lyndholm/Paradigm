import math
import os
from typing import Optional

import requests
from PIL import Image, ImageFont

from . import IMAGE_ASSETS_PATH


def download_image(url: str) -> Image.Image:
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            return Image.open(r.raw).convert('RGBA')
        else:
            return Image.open(f'{IMAGE_ASSETS_PATH}export_error.png')
    except:
        return Image.open(f'{IMAGE_ASSETS_PATH}export_error.png')


def ratio_resize(image: Image.Image, max_width: int, max_height: int) -> Image.Image:
    ratio = max(max_width / image.width, max_height / image.height)

    return image.resize(
        (int(image.width * ratio), int(image.height * ratio)),
        Image.ANTIALIAS
    )


def open_font(
    size: int,
    font: str,
    directory: Optional[str] = 'paradigm/assets/fonts/',
) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(f'{directory}{font}', size)
    except OSError:
        print(f'{font} not found, defaulted font to BurbankBigCondensed-Black.ttf')
        return ImageFont.truetype(f'{directory}BurbankBigCondensed-Black.ttf', size)
    except Exception as e:
        print(f'Failed to load font, {e}')


def merge_images(
    images: Optional[list[Image.Image]] = None,
    filename: Optional[str] = 'merged',
    extension: Optional[str] = '.png'
):
    """Merge images in cache folder."""

    if not images:
        image_extensions = ('.png', '.jpg', '.jpeg')
        files = [i for i in os.listdir('paradigm/cache') if os.path.splitext(i)[-1] in image_extensions]
        if not files:
            print('No images in cache folder, unable to merge.')
            return
        images = [Image.open(f'paradigm/cache/{img}') for img in files]

    row_number = len(images)
    rows_len = math.ceil(math.sqrt(row_number))
    columns_len = round(math.sqrt(row_number))

    mode = 'RGBA' if extension == '.png' else 'RGB'
    px = 512

    rows = rows_len * px
    columns = columns_len * px
    merged = Image.new(mode, (rows, columns))

    i = 0

    for image in images:
        merged.paste(
            image,
            ((0 + ((i % rows_len) * image.width)),
                (0 + ((i // rows_len) * image.height)))
        )
        i += 1

    try:
        merged.save(f'paradigm/images/{filename}{extension}')
    except FileNotFoundError:
        os.mkdir(f'paradigm/images/')
        merged.save(f'paradigm/images/{filename}{extension}')
