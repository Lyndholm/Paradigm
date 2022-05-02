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
