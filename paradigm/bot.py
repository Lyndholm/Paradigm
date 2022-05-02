import requests

from paradigm.utils import logger


class Paradigm:
    def __init__(self) -> None:
        self.sesion = requests.Session()
        self.logger = logger.setup_logger(__class__.__name__)
