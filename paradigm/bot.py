from paradigm.utils import logger


class Paradigm:
    def __init__(self) -> None:
        self.logger = logger.setup_logger(__class__.__name__)
