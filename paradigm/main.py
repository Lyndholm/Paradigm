import time
from typing import Any, Optional

import creator
import utils
from bot import Paradigm


bot = Paradigm()
paths_to_parse = (
    utils.BACKPACKS_PATH,
    utils.BANNERS_PATH,
    utils.EMOJIS_PATH,
    utils.EMOTES_PATH,
    utils.GLIDERS_PATH,
    utils.ITEM_WRAPS_PATH,
    utils.LOADING_SCREENS_PATH,
    utils.MUSIC_PACKS_PATH,
    utils.OUTFITS_PATH,
    # utils.PICKAXES_PATH,
    # utils.PICKAXES_ALT_PATH,
    utils.SKYDIVING_TRAILS_PATH,
    utils.SPRAYS_PATH,
    utils.STYLES_PATH,
    utils.TOYS_PATH,
)


def get_added_files() -> Optional[dict[str, Any]]:
    r = bot.sesion.get('https://benbot.app/api/v1/files/added')
    if r.status_code != 200:
        return

    return r.json()


def get_asset_properties(asset: str) -> Optional[dict[str, Any]]:
    r = bot.sesion.get(
        'https://benbot.app/api/v1/assetProperties',
        params={
            'lang': 'ru',
            'path': asset
        }
    )
    if r.status_code != 200:
        return

    data = r.json()['export_properties'][0]
    return data


def generate_asset_icons(assets_list: list, asset_path_pattern: str) -> None:
    assets = list(
        filter(
            lambda asset: asset.startswith(asset_path_pattern),
            assets_list
        )
    )
    for asset in assets:
        properties = get_asset_properties(asset)
        item = utils.define_asset_type(properties['exportType'])
        icon = creator.BaseIcon(item(**properties, fmodel_path=asset))
        icon.generate_icon()
        bot.logger.info(f'Generated: {asset}')
        time.sleep(3) # sleep for 3 seconds, we don't want to spam the api


def main() -> None:
    assets = get_added_files()

    for path in paths_to_parse:
        generate_asset_icons(assets, path)


if __name__ == '__main__':
    main()
