import time
from typing import Any

import requests

import creator
import utils


class Paradigm:
    BASE = 'https://benbot.app/api/v1/'

    def __init__(self) -> None:
        self.sesion = requests.Session()
        self.logger = utils.logger.setup_logger(__class__.__name__)
        self.assets_icons = []


    def get_added_files(self) -> dict[str, Any] | None:
        r = self.sesion.get(f'{self.BASE}files/added')
        if r.status_code != 200:
            return

        return r.json()


    def get_asset_properties(self, asset: str) -> dict[str, Any] | None:
        r = self.sesion.get(
            f'{self.BASE}assetProperties',
            params={
                'lang': 'ru',
                'path': asset
            }
        )
        if r.status_code != 200:
            return

        data = r.json()['export_properties'][0]
        return data


    def generate_asset_icons(self, assets_list: list, asset_path_pattern: str) -> None:
        icons = []
        assets_paths = list(
            filter(
                lambda asset: asset.startswith(asset_path_pattern),
                assets_list
            )
        )

        for path in assets_paths:
            properties = self.get_asset_properties(path)
            AssetType = utils.define_asset_type(properties['exportType'])
            asset = AssetType(**properties, fmodel_path=path)      

            icon = creator.BaseIcon(asset).generate_icon()
            icon.asset = asset
            icons.append(icon)
            self.logger.info(f'Generated: {asset.fmodel_path}')
            time.sleep(3) # sleep for 3 seconds, we don't want to spam the api

        self.assets_icons.extend(icons)


    def merge_icons(self) -> None:
        self.assets_icons.sort(key = lambda icon: icon.asset.sorting_priority)
        utils.merge_images(self.assets_icons, filename='newcosmetics')
        utils.clear_cache()
