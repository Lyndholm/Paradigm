import logging
import logging.handlers
import os


class CustomFormatter(logging.Formatter):
    def __init__(self) -> None:

        fmt = "[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] %(message)s"

        super().__init__(
            fmt=fmt,
            datefmt="%d-%m-%Y %H:%M:%S"
        )


def setup_logger(logger_name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    if not os.path.exists('logs/'):
        os.makedirs('logs/')

    file_handler = logging.handlers.RotatingFileHandler(
        filename=f'logs/paradigm.log',
        mode='w',
        maxBytes=1024 * 1024 * 5,  # 5 MB
        backupCount=5,
        encoding='utf-8',
    )
    file_handler.setFormatter(CustomFormatter())
    logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(CustomFormatter())
    logger.addHandler(stdout_handler)

    return logger
