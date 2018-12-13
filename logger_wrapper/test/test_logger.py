from ..log import Logger
import logging
from codegenhelper import test_root, init_test_folder, remove_test_folder, put_file
from nose import with_setup
from assertpy import assert_that

logging.basicConfig(level=logging.DEBUG)

def test_getLogger():
    logger = Logger.getLogger("test_module")

    logger.debug("debug info")
    logger.title("x").debug("debug info")



def init_logger_config():
    init_test_folder()
    put_file('logger_wrapper.cfg', test_root(), '''[handlers]
all_all
''')
    

@with_setup(init_logger_config, remove_test_folder)
def test_all_from_file():
    pass
