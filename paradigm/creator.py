import os
from datetime import datetime

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from .models import FortBaseCosmetic, FortCharacter
from .utils import OUTFITS_TEXTURES_PATH, IMAGE_ASSETS_PATH
from .utils import (change_rarity_based_on_series,
                    download_image, open_font, ratio_resize)


class BaseIcon:
    def __init__(self, asset: FortBaseCosmetic):
        self.asset = asset
        self.primary_font = 'BurbankBigRegular-Black.ttf'
        self.secondary_font = 'BurbankSmall-Black.ttf'


    def draw_icon_background(self, canvas: Image.Image) -> None:
        try:
            background = Image.open(
                f'{IMAGE_ASSETS_PATH}card_background_{self.asset.rarity.removeprefix("EFortRarity::").lower()}.png'
                )
        except FileNotFoundError:
            background = Image.open(f'{IMAGE_ASSETS_PATH}card_background_common.png')

        background = background.resize((512, 512), Image.ANTIALIAS)
        canvas.paste(background)


    def draw_icon_faceplate(self, canvas: Image.Image) -> None:
        try:
            faceplate = Image.open(
                f'{IMAGE_ASSETS_PATH}card_faceplate_{self.asset.rarity.removeprefix("EFortRarity::").lower()}.png'
                )
        except FileNotFoundError:
            faceplate = Image.open(f'{IMAGE_ASSETS_PATH}card_faceplate_common.png')

        canvas.paste(faceplate, faceplate)


    def draw_text_background(
        self,
        canvas: Image.Image,
        text: str,
        x: int,
        y: int,
        font: ImageFont,
        fill: tuple
    ) -> None:
        blurred = Image.new('RGBA', canvas.size)
        draw = ImageDraw.Draw(blurred)
        draw.text(xy=(x, y), text=text, fill=fill, font=font)
        blurred = blurred.filter(ImageFilter.BoxBlur(10))

        canvas.paste(blurred, blurred)


    def draw_asset_image(self, canvas: Image.Image):
        image = getattr(self.asset.image, 'path', None)

        if not image:
            try:
                if self.asset.__class__ is FortCharacter:
                    path = OUTFITS_TEXTURES_PATH + '-' + self.asset.definition_path.replace('_', '-').replace('HID', 'CID')
                    image = download_image(f'https://benbot.app/api/v1/exportAsset?path={path}')
            except:
                image = Image.open(f'{IMAGE_ASSETS_PATH}export_error.png')
        else:
            image = download_image(f'https://benbot.app/api/v1/exportAsset?path={image}')

        if not image: 
            return

        image = ratio_resize(image, 512, 512)
        canvas.paste(image, image)


    def draw_asset_name(self, canvas: Image.Image, draw: ImageDraw.Draw):
        text_size = 32
        text = self.asset.name.text.upper()
        if not text:
            return

        font = open_font(font=self.primary_font, size=text_size)
        text_width, text_height = font.getsize(text)
        x = (512 - text_width) / 2
        y = 420

        while text_width > 512 - 4:
            text_size = text_size - 1
            font = open_font(font=self.primary_font, size=text_size)
            text_width, text_height = font.getsize(text)
            x = (512 - text_width) / 2
    
        self.draw_text_background(canvas, text, x, y, font, (0, 0, 0, 215))
        draw.text(
            (x, y),
            text,
            (255, 255, 255),
            font=font,
            align='center',
            stroke_width=1,
            stroke_fill=(0, 0, 0)
        )


    def draw_asset_description(self, canvas: Image.Image, draw: ImageDraw.Draw):
        text_size = 14
        text = self.asset.description.text.upper()[:100] # draw the first 100 characters
        if not text:
            return

        font = open_font(font=self.secondary_font, size=text_size)
        text_width, text_height = font.getsize(text)
        x = (512 - text_width) / 2
        y = 460

        while text_width > 512 - 4:
            text_size = text_size - 1
            font = open_font(font=self.secondary_font, size=text_size)
            text_width, text_height = font.getsize(text)
            x = (512 - text_width) / 2
        
        self.draw_text_background(canvas, text, x, y, font, (0, 0, 0, 215))
        draw.text(
            (x, y),
            text=text,
            fill='white',
            font=font,
        )


    def draw_asset_tags(self, canvas: Image.Image, draw: ImageDraw.Draw, text: str):
        if not self.asset.name.text or not self.asset.description.text:
            return

        text_size = 17
        font = open_font(font='BurbankBigRegular-Black.ttf', size=text_size)

        text = '.'.join(text.split('.')[2:]).upper()
        text_width, text_height = font.getsize(text)
        self.draw_text_background(
            canvas, text, 8, 512 - 2 * 4 - text_height, font, (0, 0, 0, 215))

        draw.text(
            (8, 512 - 2 * 4 - text_height),
            text,
            fill=(167, 184, 188),
            font=font,
            align='left'
        )


    def draw_plus_sign(self, canvas: Image.Image) -> Image.Image:
        cb = Image.open(f'{IMAGE_ASSETS_PATH}plus_sign.png')
        canvas.paste(cb, cb)


    def draw_tags_and_flags(self, canvas: Image.Image, draw: ImageDraw.Draw) -> None:
        if self.asset.gameplay_tags:
            tags = list(
                filter(
                    lambda x: x.startswith('Cosmetics.Source.') or x.startswith('Athena.ItemAction.'),
                    self.asset.gameplay_tags
                )
            )
            if tags:
                self.draw_asset_tags(canvas, draw, tags[0])

            flags = list(
                filter(
                    lambda x: x.startswith('Cosmetics.UserFacingFlags.'),
                    self.asset.gameplay_tags
                )
            )
            if flags:
                self.draw_plus_sign(canvas)


    def generate_icon(self) -> Image.Image:
        canvas = Image.new('RGB', (512, 512))
        draw = ImageDraw.Draw(canvas)

        change_rarity_based_on_series(self.asset)
        
        self.draw_icon_background(canvas)
        self.draw_asset_image(canvas)
        self.draw_icon_faceplate(canvas)
        self.draw_asset_name(canvas, draw)
        self.draw_asset_description(canvas, draw)
        self.draw_tags_and_flags(canvas, draw)

        path = self.asset.path.split('/')[-1].removesuffix('.uasset')
        try:
            canvas.save(f'paradigm/cache/{self.asset.__class__.__name__}/{path}.png')
        except FileNotFoundError:
            os.mkdir(f'paradigm/cache/{self.asset.__class__.__name__}/')
            canvas.save(f'paradigm/cache/{self.asset.__class__.__name__}/{path}.png')

        return canvas
