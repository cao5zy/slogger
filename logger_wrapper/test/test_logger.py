from ..log import Logger
import logging

logging.basicConfig(level=logging.DEBUG)

def test_getLogger():
    logger = Logger.getLogger("test_module")

    logger.debug("debug info")
    logger.title("x").debug("debug info")
