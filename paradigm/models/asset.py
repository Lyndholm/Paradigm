from typing import Any

from pydantic import BaseModel

from .cosmetics import FortBaseCosmetic


class BaseAsset(BaseModel):
    import_map: list[Any]
    export_map: list[Any]
    export_properties: list[FortBaseCosmetic]
